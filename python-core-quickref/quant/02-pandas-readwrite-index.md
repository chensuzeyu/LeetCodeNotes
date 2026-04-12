# 02 · pandas 的读写与索引

完整演示：[scripts/02_pandas_readwrite_index.py](scripts/02_pandas_readwrite_index.py)  
运行：`python3 02_pandas_readwrite_index.py`

偏**CSV 读写、日期列转索引、索引再还原**；你读 `1_ETF轮动` 的 `txt` / `portfolio.csv` 链路时，脑子里要先有这张图。  
下文各「输入代码 / 输出结果」与脚本逐段对应；临时文件路径会因机器不同而变化，可用 `<TMP_PATH>` 理解。

## `read_csv`

| 用法 | 说明 |
|------|------|
| `pd.read_csv(...)` | 读入 CSV，默认给整数索引 |
| `index_col="trade_date"` | 直接把某一列设为索引 |

- `read_csv` 会尽量自动推断类型，所以纯数字日期列常会先被读成整数。

**输入代码**：

```python
csv_text = "trade_date,etf,score\n20240108,510180.SH,0.91\n20240109,159915.SZ,1.08\n"
df_plain = pd.read_csv(io.StringIO(csv_text))
df_idx = pd.read_csv(io.StringIO(csv_text), index_col="trade_date")
```

**输出结果**：

```text
read_csv -> [{'trade_date': 20240108, 'etf': '510180.SH', 'score': 0.91}, {'trade_date': 20240109, 'etf': '159915.SZ', 'score': 1.08}]
read_csv(index_col='trade_date') index -> ['20240108', '20240109']
index_col 后首行 -> {'etf': '510180.SH', 'score': 0.91}
```

## `set_index` / `reset_index`

| 用法 | 说明 |
|------|------|
| `df.set_index("trade_date")` | 把列变成索引 |
| `df.reset_index()` | 把索引还原成普通列 |

- `set_index` 返回的是新表；如果不重新赋值，原来的 `df_plain` 不会自动改变。

**输入代码**：

```python
df_set = df_plain.set_index("trade_date")
df_set.reset_index()
```

**输出结果**：

```text
set_index('trade_date') columns -> ['etf', 'score']
set_index 后索引 -> ['20240108', '20240109']
reset_index() -> [{'trade_date': 20240108, 'etf': '510180.SH', 'score': 0.91}, {'trade_date': 20240109, 'etf': '159915.SZ', 'score': 1.08}]
```

## `to_csv`

| 用法 | 说明 |
|------|------|
| `df.to_csv(path)` / `df.to_csv(path, index=False)` | 写出 CSV；默认把索引也写出去 |
| 再 `read_csv(..., index_col=...)` | 很常见的“写盘再读回”套路 |

- `to_csv` 默认会把索引写成第一列；后面读回时常要显式告诉 pandas 哪一列是索引。

**输入代码**：

```python
df_set.to_csv()
df_plain.to_csv(index=False)
df_set.to_csv(out)
read_back = pd.read_csv(out, index_col="trade_date")
```

**输出结果**：

```text
to_csv() 前两行 -> ['trade_date,etf,score', '20240108,510180.SH,0.91']
to_csv(index=False) 前两行 -> ['trade_date,etf,score', '20240108,510180.SH,0.91']
写入 -> <TMP_PATH>\quant_scores_*.csv
read back -> {20240108: {'etf': '510180.SH', 'score': 0.91}, 20240109: {'etf': '159915.SZ', 'score': 1.08}}
```

**注意点**：`to_csv()` 和 `to_csv(index=False)` 虽然表头都能看见 `trade_date`，但前者那一列来自索引，后者来自普通列。`read back` 里最外层 key 是整数 `20240108` / `20240109`，因为 `read_csv` 会把纯数字索引自动推断成整数；如果你想和 `hkcodex` / 回测脚本里的 `YYYYMMDD` 字符串完全对齐，后面通常还会显式转成字符串。

## 官方文档

- [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
- [DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)  
- [DataFrame.set_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)
