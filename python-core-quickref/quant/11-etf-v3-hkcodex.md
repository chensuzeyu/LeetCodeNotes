# 11 · ETF轮动_v3 用到的 hkcodex 全接口

完整演示：[scripts/11_etf_v3_hkcodex.py](scripts/11_etf_v3_hkcodex.py)  
运行：`python3 11_etf_v3_hkcodex.py`

本课在 [09-hkcodex-dates-marketdata](09-hkcodex-dates-marketdata.md) 的**通用返回形状**之上，按 **`13_ETF轮动_v3`** 三个脚本的**实际调用方式**逐条对照。  
现场手册（路径、cwd、缓存、风险）：[DATAFLOW.md](../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md)

## 接口总览

| 接口 | `1_1` 选股 | `1_2` 回测 | `generate` 实盘 |
|------|:----------:|:----------:|:---------------:|
| `ensure_hkcodex_path` | ✓ | ✓ | ✓ |
| `get_trade_days` | 区间 + warmup | 区间 | `until` + `count` |
| `fund_daily` | OHLC + `reset_index` | `to_datetime` + `ffill` | 截止昨日 + 保留索引 |
| `index_daily` | — | 沪深300 基准 | — |
| `analyzer` | — | 策略 vs 基准 | — |

---

## 0 · bootstrap

v3 三个脚本头部相同：自 `__file__` 向上找 `ensure_hkcodex_path.py`，执行后再 `import hkcodex as hx`。

| 要点 | 说明 |
|------|------|
| `HKCODEX_HOME` | 指向 `HKCodex-CodeSets_v3`，缓存落在 `data/` |
| `token.txt` | 与 `.pyd` 同级；无 token 时部分接口（如 `index_daily`）可能返回空 |

**输出结果**：

```text
helper -> D:\develop\Quant\HKCodex\HKCodex-CodeSets_v3\ensure_hkcodex_path.py
HKCODEX_HOME -> D:\develop\Quant\HKCodex\HKCodex-CodeSets_v3
```

---

## 1 · `get_trade_days`

### 1.1 `1_1` 策略区间（第 110 行）

```python
strategy_trade_days = hx.get_trade_days(since=start_date, until=end_date)
```

**输出结果**（`since="20240102"`, `until="20240110"`）：

```text
   cal_date pretrade_date
0  20240102      20231229
1  20240103      20240102
2  20240104      20240103
... 共 7 行
```

### 1.2 `1_1` warmup 扩日历（第 112 行）

```python
warmup_bars = max(BIAS_N, MOMENTUM_DAY, SLOPE_N, EFFICIENCY_N)  # 25
trade_days_with_warmup = hx.get_trade_days(
    until=end_date, count=len(strategy_trade_days) + warmup_bars
)
start_date = trade_days_with_warmup.iloc[0]["cal_date"]
```

**输出结果**：

```text
warmup 后总行数 -> 32
扩完 start_date -> 20231127
   cal_date pretrade_date
0  20231127      20231124
1  20231128      20231127
2  20231129      20231128
```

- `start_date` 被**改写**为 warmup 起点，`fund_daily` 从这一天开始拉，保证前 25 根 K 可算因子。
- 循环里 `for idx, day in enumerate(trade_days_with_warmup['cal_date'])`，`idx < warmup_bars` 时 `continue`，不写 txt。

### 1.3 `generate_stock_selection` 单日（第 139 行）

```python
trade_days_with_warmup = hx.get_trade_days(until=trading_date, count=warmup_bars + 60)
yesterday = current_row["pretrade_date"].iloc[0]  # 行情截止日
```

**输出结果**（`trading_date="20240110"`）：

```text
pretrade_date（行情截止日）-> 20240109
    cal_date pretrade_date
82  20240108      20240105
83  20240109      20240108
84  20240110      20240109
```

- 实盘 **不含 signal 日收盘**：`fund_daily` 的 `end_date=yesterday`（上一交易日）。

### 1.4 `1_2` 回测日历（第 154 行）

```python
trade_day = hx.get_trade_days(since=start_date, until=end_date)
g.df = pd.DataFrame(index=trade_day["cal_date"], columns=...)
```

- 回测 **不含 warmup 扩出来的早期日期**；与 `1_1` 写 txt 的 `day` 一一对应。
- 每个 `day` 读 `ETF轮动_v3/{day}.txt`。

---

## 2 · `fund_daily`

四只 ETF：`510880.SH`, `159915.SZ`, `513100.SH`, `518880.SH`；均 `adjust='front'`（前复权）。

### 2.1 `1_1` 选股（第 118 行）

```python
df = hx.fund_daily(etf=stk, start_date=start_date, end_date=end_date, adjust="front")
df_all[stk] = df[["open", "high", "low", "close"]].reset_index(drop=True)
# 循环内: history = df_all[stk].iloc[:idx]
```

**原始返回**（`510880.SH`，warmup 起点 `20231127`）：

```text
             open   high    low  close  pre_close       vol      amount
trade_date
20231127    3.002  3.006  2.987  3.000      3.009  607921.0  181918.979
20231128    2.996  2.996  2.978  2.994      3.000  478999.0  143007.650
```

**`reset_index` 后**（整数行号 ↔ 日历 `idx` 对齐）：

```text
    open   high    low  close
0  3.002  3.006  2.987  3.000
1  2.996  2.996  2.978  2.994
2  2.994  2.999  2.976  2.981
```

**注意点**：`len(df_all[stk])` 必须等于 `len(trade_days_with_warmup)`，否则 `iloc[:idx]` 与交易日错位。

### 2.2 `1_2` 回测喂 backtrader（第 179-181 行）

```python
data = hx.fund_daily(etf=stk, start_date=start_date, end_date=end_date, adjust="front")
data.index = pd.to_datetime(data.index, format="%Y%m%d")
data = data[["open", "high", "low", "close"]].ffill()
# bt.feeds.PandasData(dataname=data, ...)
```

**输出结果**（同一标的，index 变 `DatetimeIndex`）：

```text
             open   high    low  close
trade_date
2023-11-27  3.002  3.006  2.987  3.000
2023-11-28  2.996  2.996  2.978  2.994
2023-11-29  2.994  2.999  2.976  2.981
```

- 回测区间用 **`start_date/end_date` 原值**（如 `20240101`），**不**用 warmup 改写后的起点；缺 K 时用 `.ffill()` 补齐。

### 2.3 `generate` 实盘（第 155-163 行）

```python
df = hx.fund_daily(etf=stk, start_date=start_date, end_date=yesterday, adjust="front")
df_all[stk] = df[["open", "high", "low", "close"]]  # 保留 trade_date 索引
history = df_all[stk]
history = history / history.iloc[0]["close"]  # 整段归一化
```

**输出结果**（截止 `20240109`）：

```text
             open   high    low  close
trade_date
20240105    3.030  3.087  3.026  3.044
20240108    3.040  3.042  3.013  3.015
20240109    3.014  3.042  2.991  3.038

归一化后 close.tail(3):
20240105    1.000000
20240108    0.990473
20240109    0.998029
```

| 对比 | `1_1` | `generate` |
|------|-------|------------|
| 行索引 | 去掉，`iloc[:idx]` | 保留 `trade_date` |
| 行情截止 | `end_date`（策略末） | `pretrade_date`（signal 日前一日） |
| 价格尺度 | 原始前复权 | 除以首日 close |

---

## 3 · `index_daily`（仅 `1_2`）

```python
benchmark = hx.index_daily(index_code="000300.SH", start_date=start_date, end_date=end_date)
```

| 项 | 说明 |
|----|------|
| 返回 | `pd.Series`，`name='pct_chg'`，小数日涨跌幅 |
| 索引 | `DatetimeIndex`（与 `get_trade_days` 的字符串不同） |
| 用途 | 传给 `hx.analyzer` 作基准曲线 |

**输出结果**（`20240102`～`20240106`，与 09 课相同区间）：

```text
trade_date
2024-01-02   -0.013045
2024-01-03   -0.002379
2024-01-04   -0.009249
Name: pct_chg, dtype: float64
```

---

## 4 · `analyzer`（仅 `1_2`）

```python
pnl = pd.Series(result[0].analyzers._TimeReturn.get_analysis())
stats_all = hx.analyzer(pnl, benchmark, result[0], fig_name=strategy_name)
```

| 参数 | v3 传入 | 说明 |
|------|---------|------|
| `port_pnl` | backtrader `TimeReturn` 序列 | 策略日收益率 |
| `market_pnl` | `index_daily` 的 `pct_chg` | 基准日收益率 |
| `strategy` | `result[0]` | 回测策略实例（报告里取交易统计） |
| `fig_name` | `'ETF轮动_v3'` | 非空时写对比图 PNG |

**输入示意**（策略 vs 基准，各 3 日）：

```text
pnl（策略）:
2024-01-02    0.015000
2024-01-03   -0.002379
2024-01-04    0.008000

benchmark:
2024-01-02   -0.013045
2024-01-03   -0.002379
2024-01-04   -0.009249
```

**输出结果**（`stats_all` 关键字段）：

```text
stats['strategy']  -> {'days': 3.0, 'total_return': 0.020686, 'annual_return': 4.583946,
                       'annual_vol': 0.113336, 'max_drawdown': -0.002379}
stats['benchmark'] -> {'days': 3.0, 'total_return': -0.0245, 'annual_return': -0.875518,
                       'annual_vol': 0.070074, 'max_drawdown': -0.011606}
stats['figure']    -> None   # fig_name 非空时为 PNG 路径
```

- `analyzer` 内部会按日期 **align** 策略与基准；`fig_name='ETF轮动_v3'` 时在当前目录写分析图。

---

## 5 · 缓存路径（读 pkl 时对照）

| 接口 | 缓存文件模式 |
|------|-------------|
| `get_trade_days` | `data/trade_cal/trade_cal_{YYYY}.pkl` |
| `fund_daily` | `data/fund_daily/{etf}_{start}_{end}_{adjust}.pkl` |
| `index_daily` | `data/index_daily/{code}_{start}_{end}.pkl` |

根目录 = `HKCODEX_HOME`（一般为 `HKCodex-CodeSets_v3`）。

---

## 先修课顺序（读 v3）

| 顺序 | 文档 | 对应 v3 能力 |
|:----:|------|-------------|
| 1 | [09-hkcodex-dates-marketdata](09-hkcodex-dates-marketdata.md) | 接口返回形状 |
| 2 | **本文** | 三脚本各自怎么用 |
| 3 | [04-pandas-datetime-ffill-shape](04-pandas-datetime-ffill-shape.md) | `1_2` 的 `to_datetime` / `ffill` |
| 4 | [03-pandas-loc-iloc-filter-sort](03-pandas-loc-iloc-filter-sort.md) | `1_1` 的 `iloc[:idx]` |
| 5 | [08-backtrader-order-broker-analyzer](08-backtrader-order-broker-analyzer.md) | `TimeReturn` → `pnl` |
| 6 | [DATAFLOW.md](../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md) | txt / cwd / 对齐风险 |
