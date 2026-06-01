# 09 · hkcodex 的交易日与行情接口

完整演示：[scripts/09_hkcodex_dates_marketdata.py](scripts/09_hkcodex_dates_marketdata.py)  
运行：`python3 09_hkcodex_dates_marketdata.py`

偏**你在 `D:\develop\Quant` 里读脚本时会真正碰到的本地接口**：先把路径引导挂上，再看交易日、ETF 日线、指数收益序列的实际返回形状。  
本课默认你已经在 `hkcodex` Conda 环境里，并且本机有 `HKCodex-CodeSets_v3`。

下文示例区间与 **`13_ETF轮动_v3/1_1_ETF轮动_选_v3.py`** 一致：2024 年初、`510880.SH`（红利 ETF）。

## bootstrap

| 要点 | 说明 |
|------|------|
| `ensure_hkcodex_path.py` | 先把 `hkcodex` 的实现挂到当前解释器 |
| `HKCODEX_HOME` | 让缓存、`token.txt`、`data/` 能被正确找到 |

- 这一步本质上是在先把本地依赖环境接好；接口本身能不能跑，前提就是路径和家目录都对。

**输入代码**：

```python
helper = workspace / "Quant" / "HKCodex" / "HKCodex-CodeSets_v3" / "ensure_hkcodex_path.py"
os.environ["HKCODEX_HOME"] = str(helper.parent)
```

**输出结果**：

```text
helper -> <HKCODEX_HELPER>
```

## `get_trade_days`

| 用法 | 说明 |
|------|------|
| `hx.get_trade_days(since=..., until=...)` | 区间内的交易日表 |
| `hx.get_trade_days(until=..., count=N)` | 从 `until` 往前数 N 个交易日（v3 用来拉 warmup） |

- 返回 **`pd.DataFrame`**，两列都是字符串 `YYYYMMDD`；周末、法定假日不在表里。
- `cal_date`：当日；`pretrade_date`：上一交易日（跨周末时会跳号，如 `20240105 → 20240108`）。

**输入代码**（对应 v3 第 110 行）：

```python
trade_day = hx.get_trade_days(since="20240102", until="20240106")
```

**输出结果**（`trade_day.head(3)`）：

```text
   cal_date pretrade_date
0  20240102      20231229
1  20240103      20240102
2  20240104      20240103
```

**v3 还会用 `count` 往前多取 warmup 根 K 线**（第 112 行）：

```python
warmup_bars = 25
trade_days_with_warmup = hx.get_trade_days(until="20240110", count=5)
start_date = trade_days_with_warmup.iloc[0]["cal_date"]  # 最早一天，供 fund_daily 起点
```

**输出结果**（`count=5` 示意，只取 5 行便于阅读）：

```text
   cal_date pretrade_date
0  20240104      20240103
1  20240105      20240104
2  20240108      20240105
3  20240109      20240108
4  20240110      20240109
```

## `fund_daily`

| 用法 | 说明 |
|------|------|
| `hx.fund_daily(etf=..., start_date=..., end_date=..., adjust="front")` | ETF 前复权日线 |

- 返回 **`pd.DataFrame`**；**行索引**名为 `trade_date`，值为 `YYYYMMDD` 字符串。
- 常用列：`open`, `high`, `low`, `close`, `pre_close`, `vol`, `amount`。
- v3 只取 OHLC，再 **`reset_index(drop=True)`** 变成 0..n 整数行号，方便 `iloc` 切片算因子。

**输入代码**（v3 标的 `510880.SH`，对应第 118 行）：

```python
fund = hx.fund_daily(etf="510880.SH", start_date="20240102", end_date="20240106", adjust="front")
ohlc = fund[["open", "high", "low", "close"]].reset_index(drop=True)
```

**输出结果**（`fund.head(3)`，前复权价）：

```text
             open   high    low  close  pre_close         vol      amount
trade_date
20240102    2.931  2.983  2.930  2.970      2.931  1458169.89  432515.576
20240103    2.968  3.014  2.965  3.010      2.970  2441793.13  733444.176
20240104    3.008  3.040  3.003  3.034      3.010  2469679.53  747167.919
```

**v3 切片后**（`ohlc.head(3)`，无日期索引，后面 `iloc[-25:]` 算动量）：

```text
    open   high    low  close
0  2.931  2.983  2.930  2.970
1  2.968  3.014  2.965  3.010
2  3.008  3.040  3.003  3.034
```

## `index_daily`

| 用法 | 说明 |
|------|------|
| `hx.index_daily(index_code=..., start_date=..., end_date=...)` | 指数日涨跌幅序列 |

- 返回 **`pd.Series`**，不是 `DataFrame`；`name='pct_chg'`，值为小数（-0.013045 表示约 -1.30%）。
- 行索引为 **`DatetimeIndex`**（`2024-01-02`），与 `get_trade_days` 的字符串日期格式不同，对齐时要注意。

**输入代码**：

```python
index_s = hx.index_daily(index_code="000300.SH", start_date="20240102", end_date="20240106")
```

**输出结果**（`index_s.head(3)`）：

```text
trade_date
2024-01-02   -0.013045
2024-01-03   -0.002379
2024-01-04   -0.009249
Name: pct_chg, dtype: float64
```

## 下一步

- 读 **`13_ETF轮动_v3`** 时，三个脚本对同一接口的用法不同（warmup、`reset_index` vs `ffill`、`analyzer` 等），见 **[11-etf-v3-hkcodex](11-etf-v3-hkcodex.md)**。

## 本地文档

- [HKCodex README](../../../Quant/HKCodex/README.md)  
- [HKCodex Learn README](../../../Quant/HKCodex-learn/README.md)  
- [ETF轮动_v3 DATAFLOW](../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md)
