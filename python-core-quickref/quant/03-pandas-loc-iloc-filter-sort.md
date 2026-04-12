# 03 · pandas 的 loc / iloc / 筛选 / 排序

完整演示：[scripts/03_pandas_loc_iloc_filter_sort.py](scripts/03_pandas_loc_iloc_filter_sort.py)  
运行：`python3 03_pandas_loc_iloc_filter_sort.py`

偏**读量化脚本时最常见的“从表里拿出我要的那一行 / 那几列 / 那一批记录”**。  
下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文。

## `loc` / `iloc`

| 用法 | 说明 |
|------|------|
| `df.loc[label]` | 按索引标签取 |
| `df.iloc[pos]` | 按位置取 |

- `loc` 看的是标签语义，`iloc` 看的是物理位置语义；两者别混成“都像列表下标”。

**输入代码**：

```python
df.loc["20240109"]
df.iloc[1]
```

**输出结果**：

```text
df.loc['20240109'].to_dict(orient='records') -> [{'etf': '159915.SZ', 'score': 1.08}, {'etf': '513100.SH', 'score': 1.02}]
df.iloc[1].to_dict() -> {'etf': '159915.SZ', 'score': 1.08}
```

**注意点**：当某个索引标签对应多行时，`df.loc["20240109"]` 返回的不是单行 `Series`，而是一个子 `DataFrame`。

## 布尔筛选

| 用法 | 说明 |
|------|------|
| `df[df["score"] > 1.0]` | 先筛行 |
| `[..., ["etf", "score"]]` | 再裁列 |

- 布尔筛选最核心的是先得到一个同长度布尔条件，再拿它筛行。

**输入代码**：

```python
picked = df.loc[df["score"] > 1.0, ["etf", "score"]]
```

**输出结果**：

```text
df[df['score'] > 1.0][['etf', 'score']] -> [{'etf': '159915.SZ', 'score': 1.08}, {'etf': '513100.SH', 'score': 1.02}]
```

## 排序 / 去重

| 用法 | 说明 |
|------|------|
| `sort_values("score")` | 默认升序 |
| `sort_values("score", ascending=False)` | 按分数从高到低排 |
| `drop_duplicates(subset=["etf"])` | 每个 ETF 只保留一行 |

- `drop_duplicates(..., keep="first")` 会保留当前顺序里的第一条，所以常和 `sort_values(...)` 连起来用。

**输入代码**：

```python
sorted_asc = df.sort_values("score")
sorted_df = df.sort_values("score", ascending=False)
dedup = sorted_df.drop_duplicates(subset=["etf"], keep="first")
```

**输出结果**：

```text
sort_values('score') -> [{'trade_date': '20240110', 'etf': '159915.SZ', 'score': 0.88}, {'trade_date': '20240108', 'etf': '510180.SH', 'score': 0.91}, {'trade_date': '20240109', 'etf': '513100.SH', 'score': 1.02}, {'trade_date': '20240109', 'etf': '159915.SZ', 'score': 1.08}]
sort_values('score', ascending=False) -> [{'trade_date': '20240109', 'etf': '159915.SZ', 'score': 1.08}, {'trade_date': '20240109', 'etf': '513100.SH', 'score': 1.02}, {'trade_date': '20240108', 'etf': '510180.SH', 'score': 0.91}, {'trade_date': '20240110', 'etf': '159915.SZ', 'score': 0.88}]
drop_duplicates(subset=['etf']) -> [{'trade_date': '20240109', 'etf': '159915.SZ', 'score': 1.08}, {'trade_date': '20240109', 'etf': '513100.SH', 'score': 1.02}, {'trade_date': '20240108', 'etf': '510180.SH', 'score': 0.91}]
```

## 官方文档

- [DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)  
- [DataFrame.iloc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)  
- [DataFrame.sort_values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
