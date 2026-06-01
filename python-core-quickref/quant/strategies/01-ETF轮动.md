# 策略索引 · 1_ETF轮动

> 薄索引卡：技能细节在 quant 分册；**完整数据流在 HKCodex 策略目录**。

| 项 | 链接 |
|----|------|
| **现场手册（主笔记）** | [`DATAFLOW.md`](../../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md) |
| 选股脚本 | `.../1_ETF轮动/1_1_ETF轮动_选.py` |
| 回测脚本 | `.../1_ETF轮动/1_2_ETF轮动_回测.py` |
| 聚宽迁移 | `.../1_ETF轮动/聚宽迁移说明.md` |

## 一句话

四 ETF、25 日 log 回归动量 × R²，日频持最强一只；信号在 `ETF轮动/*.txt`，回测开盘调仓。

## 建议先修的 quant 课

| 顺序 | 文档 | 对应能力 |
|:----:|------|----------|
| 1 | [01-pandas-series-dataframe](../01-pandas-series-dataframe.md) | `Series`、`DataFrame`；含 `1_1` 第 65 行 `scores` / `idxmax` |
| 2 | [03-pandas-loc-iloc-filter-sort](../03-pandas-loc-iloc-filter-sort.md) | `iloc`、行切片；含 `1_1` 第 67 行 `df_all[stk].iloc[...]['close']` |
| 3 | [06-numpy-polyfit-score](../06-numpy-polyfit-score.md) | 得分公式 |
| 4 | [09-hkcodex-dates-marketdata](../09-hkcodex-dates-marketdata.md) | `get_trade_days`、`fund_daily` |
| 5 | [10-1etf-chain](../10-1etf-chain.md) | txt 读写、`cwd`、portfolio |

回测细读再加 [07](../07-backtrader-cerebro-data-strategy.md)、[08](../08-backtrader-order-broker-analyzer.md)。

## 状态

- [x] `DATAFLOW.md` 已建（2026-05-23）
- [ ] 其他策略待补索引卡
