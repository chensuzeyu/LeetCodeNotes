# 09 · hkcodex 的交易日与行情接口

完整演示：[scripts/09_hkcodex_dates_marketdata.py](scripts/09_hkcodex_dates_marketdata.py)  
运行：`python3 09_hkcodex_dates_marketdata.py`

偏**你在 `D:\develop\Quant` 里读脚本时会真正碰到的本地接口**：先把路径引导挂上，再看交易日、ETF 日线、指数收益序列的实际返回形状。  
本课默认你已经在 `hkcodex` Conda 环境里，并且本机有 `HKCodex-CodeSets_v3`。

## bootstrap

| 要点 | 说明 |
|------|------|
| `ensure_hkcodex_path.py` | 先把 `hkcodex` 的实现挂到当前解释器 |
| `HKCODEX_HOME` | 让缓存、`token.txt`、`data/` 能被正确找到 |

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
| `hx.get_trade_days(since=..., until=...)` | 返回交易日表 |

**输入代码**：

```python
trade_day = hx.get_trade_days(since="20240102", until="20240110")
```

**输出结果**：

```text
columns -> ['cal_date', 'pretrade_date']
cal_date -> ['20240102', '20240103', '20240104', '20240105', '20240108', '20240109', '20240110']
```

## `fund_daily`

| 用法 | 说明 |
|------|------|
| `hx.fund_daily(etf=..., start_date=..., end_date=..., adjust="front")` | ETF 日线 |

**输入代码**：

```python
fund = hx.fund_daily(etf="510180.SH", start_date="20240102", end_date="20240110", adjust="front")
```

**输出结果**：

```text
fund shape -> (0, 0)
fund columns -> []
fund index sample -> []
fund is empty -> True
```

**注意点**：当前这台机器的固定示例区间下，`fund_daily` 返回了空表。教学重点先放在“调用姿势”和“返回对象是 `DataFrame`”上；换区间、换缓存或换数据源后，真实策略里看到的通常会是带 OHLC 列的表。

## `index_daily`

| 用法 | 说明 |
|------|------|
| `hx.index_daily(index_code=..., start_date=..., end_date=...)` | 指数收益序列 |

**输入代码**：

```python
index_df = hx.index_daily(index_code="000300.SH", start_date="20240102", end_date="20240110")
```

**输出结果**：

```text
index type -> Series
index name -> pct_chg
index sample -> []
pct_chg head -> []
```

**注意点**：`HKCodex-learn` 里这个接口返回的是 `Series`，不是 `DataFrame`；你后面在回测脚本里看到它被直接当收益序列喂给分析函数，就是因为这个返回形状。

## 本地文档

- [HKCodex README](/d:/develop/Quant/HKCodex/README.md)  
- [HKCodex Learn README](/d:/develop/Quant/HKCodex-learn/README.md)
