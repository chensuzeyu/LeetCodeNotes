# 策略索引 · 13_ETF轮动_v3

> 薄索引卡：技能细节在 quant 分册；**完整数据流在 HKCodex 策略目录**。

| 项 | 链接 |
|----|------|
| **现场手册（主笔记）** | [`DATAFLOW.md`](../../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md) |
| 批量选股 | `.../13_ETF轮动_v3/1_1_ETF轮动_选_v3.py` |
| 本地回测 | `.../13_ETF轮动_v3/1_2_ETF轮动_回测.py` |
| 实盘单日 | `.../13_ETF轮动_v3/generate_stock_selection.py` |
| 上游参考 | [1_ETF轮动/DATAFLOW.md](../../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md) |

## 一句话

四 ETF、三因子（乖离 / 斜率 / 效率）Z-Score 加权 + **1.5× 调仓阈值**；`1_1` 写 `ETF轮动_v3/*.txt`，`1_2` 开盘调仓回测。

## 建议先修的 quant 课

| 顺序 | 文档 | 对应能力 |
|:----:|------|----------|
| 1 | [01-pandas-series-dataframe](../01-pandas-series-dataframe.md) | `factor_df`、`combined_scores` |
| 2 | [03-pandas-loc-iloc-filter-sort](../03-pandas-loc-iloc-filter-sort.md) | `iloc[:idx]` 行情切片 |
| 3 | [04-pandas-datetime-ffill-shape](../04-pandas-datetime-ffill-shape.md) | 回测 `to_datetime` / `ffill` |
| 4 | [06-numpy-polyfit-score](../06-numpy-polyfit-score.md) | 斜率动量 `LinearRegression` |
| 5 | [09-hkcodex-dates-marketdata](../09-hkcodex-dates-marketdata.md) | hkcodex 返回形状 |
| 6 | **[11-etf-v3-hkcodex](../11-etf-v3-hkcodex.md)** | **v3 三脚本 hkcodex 用法对照** |
| 7 | [08-backtrader-order-broker-analyzer](../08-backtrader-order-broker-analyzer.md) | `TimeReturn`、`analyzer` |

回测框架细读再加 [07](../07-backtrader-cerebro-data-strategy.md)。

## hkcodex 在本策略中的位置

| 接口 | 脚本 |
|------|------|
| `get_trade_days` | 三脚本均有，用法不同（见 [11 课](../11-etf-v3-hkcodex.md)） |
| `fund_daily` | 三脚本均有，切片方式不同 |
| `index_daily` | 仅 `1_2` |
| `analyzer` | 仅 `1_2` |

## 状态

- [x] `DATAFLOW.md` 已建（2026-05-26）
- [x] LeetCodeNotes [11-etf-v3-hkcodex](../11-etf-v3-hkcodex.md) 已建
