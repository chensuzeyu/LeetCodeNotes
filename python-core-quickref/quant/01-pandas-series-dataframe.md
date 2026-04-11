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
| `s.index` / `s.name` | 查看索引和名称 |

**输入代码**：

```python
s = pd.Series([0.91, 1.08, 0.97], index=["510180.SH", "159915.SZ", "513100.SH"], name="score")
```

**输出结果**：

```text
Series.to_dict() -> {'510180.SH': 0.91, '159915.SZ': 1.08, '513100.SH': 0.97}
Series.index -> ['510180.SH', '159915.SZ', '513100.SH']
Series.name -> score
```

## DataFrame

| 用法 | 说明 |
|------|------|
| `pd.DataFrame({...}, index=...)` | 二维表，最常见的量化中间结果载体 |
| `df.columns` / `df.index` | 看列名与索引 |
| `df.to_dict(orient="index")` | 快速看“索引 → 一整行” |

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
columns -> ['etf', 'score', 'hold']
index -> ['20240108', '20240109']
```

## 列访问 / head

| 用法 | 说明 |
|------|------|
| `df["score"]` | 取单列，返回 `Series` |
| `df[["etf", "score"]]` | 取多列，返回 `DataFrame` |
| `df.head(1)` | 看前几行 |

**输入代码**：

```python
df["score"].tolist()
df[["etf", "score"]].to_dict(orient="records")
df.head(1).to_dict(orient="index")
```

**输出结果**：

```text
df['score'].tolist() -> [0.91, 1.08]
df[['etf', 'score']].to_dict(orient='records') -> [{'etf': '510180.SH', 'score': 0.91}, {'etf': '159915.SZ', 'score': 1.08}]
df.head(1).to_dict(orient='index') -> {'20240108': {'etf': '510180.SH', 'score': 0.91, 'hold': False}}
```

## 官方文档

- [pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)  
- [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
