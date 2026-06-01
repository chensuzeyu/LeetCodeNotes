# 10 · `1_ETF轮动` 的 txt 链路与产物

完整演示：[scripts/10_1etf_chain.py](scripts/10_1etf_chain.py)  
运行：`python3 10_1etf_chain.py`

偏**把 `1_1_ETF轮动_选.py` 和 `1_2_ETF轮动_回测.py` 串成一条最小可视化链路**：选股脚本写 `txt`，回测脚本按同一批日期读 `txt`，最后产出 `portfolio.csv`。  
本课不直接改原仓库文件，只做一个最小模拟，让你先把数据流顺下来。

## 真实脚本入口

| 文件 | 作用 |
|------|------|
| `1_1_ETF轮动_选.py` | 负责写每天的持仓 `txt` |
| `1_2_ETF轮动_回测.py` | 负责按日期读 `txt` 并产出组合结果 |

- 这一节的重点是把“选股产物 -> 回测输入 -> 组合结果”这条链路串起来，而不是死记某一行代码。

**输出结果**：

```text
select_script -> 1_1_ETF轮动_选.py
backtest_script -> 1_2_ETF轮动_回测.py
```

## 写 `txt`

| 要点 | 说明 |
|------|------|
| 相对目录 `ETF轮动/` | 选股结果按交易日写成一个个文本文件 |
| 每天一个 `YYYYMMDD.txt` | 里面通常是一行或多行标的代码 |

- 这里的文件名就是“交易日键”；后面回测脚本能否正确读到，很依赖这个命名约定。

**输入代码**：

```python
selected = {
    "20240108": ["159915.SZ"],
    "20240109": ["510180.SH"],
}
```

**输出结果**：

```text
demo cwd -> <CWD>\_tmp_1etf_chain_demo
相对路径 'ETF轮动/20240108.txt' 落到 -> <CWD>\_tmp_1etf_chain_demo\ETF轮动\20240108.txt
txt files -> ['20240108.txt', '20240109.txt']
```

**注意点**：这里故意把“相对路径最终落到哪里”打印出来，就是为了让你建立 `cwd` 直觉。脚本里写的是 `ETF轮动/20240108.txt`，真正能不能找到文件，取决于你运行时站在哪个目录。

## 读 `txt`

| 要点 | 说明 |
|------|------|
| 回测脚本按交易日逐天读 | 日期必须和选股脚本对齐 |
| `line.strip()` | 去掉换行符，得到标的代码列表 |

- 这一步本质上是在把文本文件重新还原成“日期 -> 标的列表”的内存结构。

**输入代码**：

```python
for day in selected:
    with open(out_dir / f"{day}.txt", "r", encoding="utf-8") as fh:
        loaded[day] = [line.strip() for line in fh]
```

**输出结果**：

```text
loaded selections -> {'20240108': ['159915.SZ'], '20240109': ['510180.SH']}
日期完全对齐 -> True
```

## `portfolio.csv`

| 要点 | 说明 |
|------|------|
| 回测结果通常会整理成一个日度持仓表 | 常见列有 `hold*`、`cash`、`value` |
| `to_csv(...)` | 写成最终产物；本课只模拟它会写到哪里 |

- `portfolio.csv` 更像回测结果的汇总产物；它不是输入，而是整条链路最后落盘的结果。

**输入代码**：

```python
csv_buffer = io.StringIO()
portfolio.to_csv(csv_buffer)
```

**输出结果**：

```text
portfolio columns -> ['hold1', 'cash', 'value']
portfolio index -> ['20240108', '20240109']
portfolio logical path -> <CWD>\_tmp_1etf_chain_demo\ETF轮动_portfolio.csv
```

## 本地脚本参考

- [`1_1_ETF轮动_选.py`](../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/1_1_ETF轮动_选.py)  
- [`1_2_ETF轮动_回测.py`](../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/1_2_ETF轮动_回测.py)

## 完整数据流（策略主笔记）

本课只演示 **txt 读写与 cwd**。变量语义、`df_all`、tushare 缓存、`iloc` 对齐等见：

- **[1_ETF轮动/DATAFLOW.md](../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md)**（HKCodex，与代码同仓）  
- [strategies/01-ETF轮动.md](strategies/01-ETF轮动.md)（本仓库索引卡）
