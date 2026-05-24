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
- **与 `dict` 的区别（简介）**：`dict` 的键 **必须唯一**，同键再赋值会 **覆盖**；`DataFrame` / `Series` 的 **index 允许重复**，同一标签可对应多行，`df.loc[标签]` 会一次取出 **所有匹配行**（见下方 `20240109` 两行）。外层 `df_all[stk]` 仍是标准库 `dict`，键（ETF 代码）唯一；表内行 index 才走 pandas 规则。`1_ETF轮动` 单只 ETF 行情通常 **一日一行**，故算分用 `iloc` 按位置切，见本课下一节。

**输入代码**（演示表在 [scripts/03_pandas_loc_iloc_filter_sort.py](scripts/03_pandas_loc_iloc_filter_sort.py) 开头；`20240109` 故意出现两次）：

```python
df = pd.DataFrame(
    {
        "trade_date": ["20240108", "20240109", "20240109", "20240110"],
        "etf": ["510180.SH", "159915.SZ", "513100.SH", "159915.SZ"],
        "score": [0.91, 1.08, 1.02, 0.88],
    }
).set_index("trade_date")

df.loc["20240109"]   # index 重复 → 子 DataFrame（2 行）
df.iloc[1]           # 按位置 → 始终 1 行
```

**输出结果**（`to_dict` 仅便于打印；`orient='records'` 含义见 [01-pandas-series-dataframe · DataFrame](01-pandas-series-dataframe.md#dataframe)）：

```text
df.loc['20240109'].to_dict(orient='records') -> [{'etf': '159915.SZ', 'score': 1.08}, {'etf': '513100.SH', 'score': 1.02}]
df.iloc[1].to_dict() -> {'etf': '159915.SZ', 'score': 1.08}
```

**注意点**：当某个索引标签对应多行时，`df.loc["20240109"]` 返回的不是单行 `Series`，而是一个子 `DataFrame`。

## `iloc` 行切片 + 取列（1_ETF轮动）

`1_1_ETF轮动_选.py` 第 67 行不是 Python 标准库，而是 **`dict` 取表 + pandas 链式取值**：

```python
temp_close = df_all[stk].iloc[idx - reg_num : idx]["close"]
```

| 片段 | 来源 | 作用 |
|------|------|------|
| `df_all[stk]` | 标准库 **`dict`** | `df_all` 是 `{ETF代码: DataFrame}`，取出该 ETF 行情表 |
| `.iloc[i:j]` | **pandas** | 按 **行位置** 切片，规则同列表：**左闭右开**，不含下标 `j` |
| `["close"]` | **pandas** | 从子表取 `close` 列 → **`Series`**，index 仍是行索引（交易日） |

| 用法 | 说明 |
|------|------|
| `df.iloc[a:b]` | 取第 `a` … `b-1` 行（不看 index 标签是什么） |
| `df.iloc[a:b]["col"]` | 先切行，再取单列；等价于 `df.iloc[a:b][["col"]]` 后.squeeze 的常用写法 |
| `df_all[code].iloc[...]` | 先 dict 定位标的，再对 **该标的** 的 DataFrame 做 `iloc` |

**输入代码**（示意 8 个交易日、`reg_num=3`、`idx=5`，与策略「不含当日」一致）：

```python
bars = pd.DataFrame(
    {"close": [3.50, 3.52, 3.55, 3.53, 3.58, 3.60, 3.62, 3.65]},
    index=["20240102", "20240103", "20240105", "20240108",
           "20240109", "20240110", "20240111", "20240112"],
)
df_all = {"510180.SH": bars}
stk, reg_num, idx = "510180.SH", 3, 5
temp_close = df_all[stk].iloc[idx - reg_num : idx]["close"]
```

**输出结果**：

```text
temp_close.index -> ['20240105', '20240108', '20240109']
temp_close.tolist() -> [3.55, 3.53, 3.58]
len(temp_close) -> 3
type(temp_close) -> Series
```

- 下标 `idx=5` 对应行 `20240110`，切片 `iloc[2:5]` 取 **第 2、3、4 行**（`20240105`、`20240108`、`20240109`），**不含** 第 5 行 `20240110`（当日）。完整时间对齐见 [`1_ETF轮动/DATAFLOW.md`](file:///E:/develop/Quant/HKCodex/HKCodex-CodeSets_v3/1_ETF轮动/DATAFLOW.md) §5.3.2。

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
