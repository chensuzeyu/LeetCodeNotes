# 量化策略 · 笔记索引

策略的 **完整数据流、路径、缓存、对齐风险** 写在 **HKCodex 各策略目录的 `DATAFLOW.md`**（与代码同仓，改脚本时同步改）。

本目录只做 **导航 + 先修课表**，避免与 `../01～10` 技能课重复。

## 策略列表

| 编号 | HKCodex 目录 | 现场手册 | 索引卡 |
|:----:|--------------|----------|--------|
| 1 | `1_ETF轮动` | [DATAFLOW.md](../../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md) | [01-ETF轮动.md](./01-ETF轮动.md) |
| 13 | `13_ETF轮动_v3` | [DATAFLOW.md](../../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md) | [13-ETF轮动_v3.md](./13-ETF轮动_v3.md) |

新增策略时：在 HKCodex 对应目录新建 `DATAFLOW.md`，在本表加一行，并增加 `NN-策略简称.md` 索引卡。

## 两层笔记分工

| 层级 | 位置 | 写什么 |
|------|------|--------|
| 技能 | `../01～10` + `scripts/` | pandas / numpy / backtrader / hkcodex 通用读法 |
| 策略 | `HKCodex/.../DATAFLOW.md` | 本策略文件、变量、数据流、cwd、缓存、风险 |
| 索引 | 本目录 `NN-*.md` | 链接 + 先修课顺序 |
