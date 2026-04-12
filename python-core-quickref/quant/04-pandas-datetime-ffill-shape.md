# 04 · pandas 的日期索引 / ffill / shape

完整演示：[scripts/04_pandas_datetime_ffill_shape.py](scripts/04_pandas_datetime_ffill_shape.py)  
运行：`python3 04_pandas_datetime_ffill_shape.py`

偏**行情表最常见的三步**：日期列转 `DatetimeIndex`、缺失值补齐、再转回 `YYYYMMDD` 字符串索引。  
这是你读 `1_2_ETF轮动_回测.py` 里 `pd.to_datetime(...).ffill()` 时最需要先熟的部分。

## `to_datetime` / `DatetimeIndex`

| 用法 | 说明 |
|------|------|
| `pd.to_datetime(index, format="%Y%m%d")` | 把字符串日期转成真正的时间索引 |
| `df.shape` | 看行列维度 |

- 一旦索引变成 `DatetimeIndex`，后面很多按时间切片、对齐、重采样操作都会更自然。

**输入代码**：

```python
dt_df = raw.copy()
dt_df.index = pd.to_datetime(dt_df.index, format="%Y%m%d")
```

**输出结果**：

```text
index class -> DatetimeIndex
DatetimeIndex -> ['2024-01-08', '2024-01-09', '2024-01-10']
shape -> (3, 2)
```

## `ffill`

| 用法 | 说明 |
|------|------|
| `df.ffill()` | 用前一个非空值向前补齐 |

- `ffill` 只会用“前一个已有值”补后面的空位，不会反过来用后值补前值。

**输入代码**：

```python
filled = dt_df[["open", "close"]].ffill()
```

**输出结果**：

```text
原始 close -> [10.1, nan, 10.4]
ffill 后 close -> [10.1, 10.1, 10.4]
```

**注意点**：量化脚本里对齐多只标的、补齐停牌或缺失行情时，`ffill` 很常见，但要先想清楚“补齐是否符合你的策略含义”。

## `strftime`

| 用法 | 说明 |
|------|------|
| `index.strftime("%Y%m%d")` | 把时间索引转回策略里常见的字符串日期 |

- 很多量化脚本最终还是用 `YYYYMMDD` 字符串做键，所以常在中途用 `DatetimeIndex`，最后再转回字符串。

**输入代码**：

```python
yyyymmdd_df.index = yyyymmdd_df.index.strftime("%Y%m%d")
```

**输出结果**：

```text
string index -> ['20240108', '20240109', '20240110']
to_dict(orient='index') -> {'20240108': {'open': 10.0, 'close': 10.1}, '20240109': {'open': 10.2, 'close': 10.1}, '20240110': {'open': 10.3, 'close': 10.4}}
```

## 官方文档

- [pandas.to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)  
- [DataFrame.ffill](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html)
