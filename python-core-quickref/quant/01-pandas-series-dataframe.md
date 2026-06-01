# 01 · pandas 的 Series / DataFrame

完整演示：[scripts/01_pandas_series_dataframe.py](scripts/01_pandas_series_dataframe.py)  
运行：`python3 01_pandas_series_dataframe.py`（在 `quant/scripts` 目录）

偏**量化脚本里最常见的数据容器**：分数表、持仓表、行情表，几乎都从 `Series` / `DataFrame` 开始。  
下文各「输入代码 / 输出结果」与脚本中的赋值及 `print` **一一对应**；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## Series

| 用法 | 说明 |
|------|------|
| `pd.Series(data, index=..., name=...)` | 一维带索引数据 |
| `s.to_dict()` | 快速看“索引 → 值”映射 |
| `s.tolist()` | 只看值，不看索引 |
| `s.index` / `s.name` | 查看索引和名称 |

- `Series` 可以理解成“带索引的一列数据”；量化里常拿它表示单个时点的打分序列或收益序列。

**输入代码**：

```python
s = pd.Series([0.91, 1.08, 0.97], index=["510180.SH", "159915.SZ", "513100.SH"], name="score")
```

**输出结果**：

```text
Series.to_dict() -> {'510180.SH': 0.91, '159915.SZ': 1.08, '513100.SH': 0.97}
Series.tolist() -> [0.91, 1.08, 0.97]
Series.index -> ['510180.SH', '159915.SZ', '513100.SH']
Series.name -> score
```

## 空 Series 填分 + idxmax（1_ETF轮动）

`1_1_ETF轮动_选.py` 第 65 行：先建 **四格空积分榜**，内层循环按 ETF 代码填分，再用 `idxmax()` 选当日持仓。

| 用法 | 说明 |
|------|------|
| `pd.Series(index=etf_libs, dtype='float64')` | 只指定 **index**（四只 ETF 代码），值先为 `NaN`；`dtype` 声明格子存浮点分 |
| `scores[stk] = ...` | 按代码写入该只 ETF 的得分（与 `dict[stk]=` 相同写法） |
| `scores.idxmax()` | 返回 **分数最大** 对应的 index（即 ETF 代码）；并列时取 index 里 **第一个** 最大值 |
| `scores.sort_values(ascending=False)` | 调试时按分从高到低查看（`DATAFLOW` §5.3.5） |

**输入代码**（与 `etf_libs` 顺序一致，分数为示意）：

```python
etf_libs = ["510180.SH", "159915.SZ", "513100.SH", "518880.SH"]
scores = pd.Series(index=etf_libs, dtype="float64")
for stk, val in zip(etf_libs, [12.3, 8.1, 45.6, 3.2]):
    scores[stk] = val
winner = scores.idxmax()
```

**输出结果**：

```text
scores.idxmax() -> 513100.SH
```

**为何本脚本用 Series 而不是 `dict`**

- 全文已在用 pandas（`fund_daily`、`close` 切片等），积分榜也用 **「代码 → 一个数」** 的 `Series`，风格一致。
- 选股一句 `idxmax()`、调试 `sort_values()` 是量化里常见写法。
- 按 `etf_libs` 顺序建表时，并列最高与 `dict` + `max(..., key=...)`（插入顺序）可对齐；**并非 dict 做不到**，此处选 Series 主要是顺手与可读。

现场数据流见 [`1_ETF轮动/DATAFLOW.md`](../../../Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md) §5.3.1 中层。

## DataFrame

| 用法 | 说明 |
|------|------|
| `pd.DataFrame({...}, index=...)` | 二维表，最常见的量化中间结果载体 |
| `df.columns` / `df.index` | 看列名与索引 |
| `df.to_dict(orient="index")` / `orient="records"` | 快速看“索引 → 一整行”或“按行记录列表” |

- `DataFrame` 更像二维表：行索引常是日期，列名常是字段名，如 `close`、`score`、`hold`。
- **index 与 `dict` 键**：`dict` 同键会覆盖；pandas 的 **index 可重复**，`loc[标签]` 可能返回多行（详见 [03-pandas-loc-iloc-filter-sort · loc/iloc](03-pandas-loc-iloc-filter-sort.md#loc--iloc)）。

**输入代码**：

```python
df = pd.DataFrame(
    {
        "etf": ["510180.SH", "159915.SZ"],
        "score": [0.91, 1.08],
        "hold": [False, True],
    },
    index=["20240108", "20240109"],
)
```

**输出结果**：

```text
DataFrame.to_dict(orient='index') -> {'20240108': {'etf': '510180.SH', 'score': 0.91, 'hold': False}, '20240109': {'etf': '159915.SZ', 'score': 1.08, 'hold': True}}
DataFrame.to_dict(orient='records') -> [{'etf': '510180.SH', 'score': 0.91, 'hold': False}, {'etf': '159915.SZ', 'score': 1.08, 'hold': True}]
columns -> ['etf', 'score', 'hold']
index -> ['20240108', '20240109']
```

## 列访问 / head

| 用法 | 说明 |
|------|------|
| `df["score"]` | 取单列，返回 `Series` |
| `df[["etf", "score"]]` | 取多列，返回 `DataFrame` |
| `df.head(1)` | 看前几行 |

- 单中括号取单列，结果是 `Series`；双中括号取多列，结果还是 `DataFrame`。

**输入代码**：

```python
df["score"].tolist()
type(df["score"])
type(df[["etf", "score"]])
df[["etf", "score"]].to_dict(orient="records")
df.head(1).to_dict(orient="index")
```

**输出结果**：

```text
df['score'].tolist() -> [0.91, 1.08]
type(df['score']) -> Series
type(df[['etf', 'score']]) -> DataFrame
df[['etf', 'score']].to_dict(orient='records') -> [{'etf': '510180.SH', 'score': 0.91}, {'etf': '159915.SZ', 'score': 1.08}]
df.head(1).to_dict(orient='index') -> {'20240108': {'etf': '510180.SH', 'score': 0.91, 'hold': False}}
```

## 官方文档

- [pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)  
- [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
