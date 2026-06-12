# 01 · pandas 的 Series / DataFrame

完整演示：[scripts/01_pandas_series_dataframe.py](scripts/01_pandas_series_dataframe.py)  
运行：`python3 01_pandas_series_dataframe.py`（在 `quant/scripts` 目录）

偏**量化脚本里最常见的数据容器**：分数表、持仓表、行情表、因子表，几乎都从 `Series` / `DataFrame` 开始。  
下文各「输入代码 / 输出结果」与脚本中的赋值及 `print` **一一对应**；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

**本课覆盖**：`1_ETF轮动` 的积分榜 + `13_ETF轮动_v3` 三脚本（`1_1` / `1_2` / `generate_stock_selection`）里出现的 **Series / DataFrame 构造与表级运算**。`iloc` 切片、`loc` 赋值、`ffill`、`rolling` 等分别在 [03](03-pandas-loc-iloc-filter-sort.md)、[02](02-pandas-readwrite-index.md)、[04](04-pandas-datetime-ffill-shape.md) 细讲。

## Series

| 用法 | 说明 |
|------|------|
| `pd.Series(data, index=..., name=...)` | 一维带索引数据 |
| `s.to_dict()` | 快速看“索引 → 值”映射 |
| `s.tolist()` | 只看值，不看索引 |
| `s.index` / `s.name` | 查看索引和名称 |
| `s.get(key, default)` | 按 index 取值，缺失时返回 default（v3 查昨日持仓得分） |

- `Series` 可以理解成“带索引的一列数据”；量化里常拿它表示单个时点的打分序列或收益序列。
- `print(s)` 左侧是 **index 标签**，右侧是值；**不是** DataFrame 的列名。

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

## Series 构造对照（13_ETF轮动_v3 常见）

v3 里至少出现 **四种** 构造方式；index 从哪来是读懂 `weights`、`combined_scores` 的关键。

| 方式 | 代码 | index 是什么 | v3 出现位置 |
|------|------|--------------|-------------|
| **dict → Series** | `pd.Series({'bias': 0.2, ...}, dtype='float64')` | dict 的 **key**（因子名） | `weights = pd.Series(FACTOR_WEIGHTS, ...)` |
| **list，无 index** | `pd.Series([0.2, 0.3, 0.5])` | 默认 **0, 1, 2** | 无（对比用；勿与 `mul` 列对齐混用） |
| **list + 显式 index** | `pd.Series([...], index=[...], name=...)` | 手动指定（ETF 代码等） | 积分榜示意 |
| **只指定 index** | `pd.Series(index=etf_libs, dtype='float64')` | 先空表，值 `NaN` | `1_ETF轮动` 积分榜 |
| **标量 + index** | `pd.Series(0, index=series.index)` | 沿用原 index，值全为 0 | `zscore` 标准差为 0 时 |
| **dict（分析器）** | `pd.Series(analyzer_dict)` | dict 的 key（日期字符串） | `1_2` 的 `pnl` |

**输入代码**：

```python
from_dict = pd.Series({"bias": 0.2, "slope": 0.3, "efficiency": 0.5}, dtype="float64")
from_list = pd.Series([0.2, 0.3, 0.5])
```

**输出结果**：

```text
dict 构造 index -> ['bias', 'slope', 'efficiency']
dict 构造:
 bias          0.2
slope         0.3
efficiency    0.5
list 默认 index -> [0, 1, 2]
list 默认:
 0    0.2
1    0.3
2    0.5
```

**注意点**：`FACTOR_WEIGHTS` 用 dict 构造时，`bias` 等是 **index**，不是列。后面 `z_factors.mul(weights, axis=1)` 靠 **列名 = weights 的 index** 对齐。

## dict 权重 + 归一化（13_ETF轮动_v3 · weights）

`1_1` / `generate_stock_selection` 第 123～124 行（或等价位置）：

| 用法 | 说明 |
|------|------|
| `pd.Series(FACTOR_WEIGHTS, dtype='float64')` | dict key → index |
| `weights / weights.sum()` | 归一化，保证权重和为 1 |
| `type(weights)` | `Series`，不是 DataFrame |

**输入代码**：

```python
FACTOR_WEIGHTS = {"bias": 0.2, "slope": 0.3, "efficiency": 0.5}
weights = pd.Series(FACTOR_WEIGHTS, dtype="float64")
weights = weights / weights.sum()
```

**输出结果**：

```text
weights:
 bias          0.2
slope         0.3
efficiency    0.5
type(weights) -> Series
weights.sum() -> 1.0
```

（本例三项已和为 1，归一化前后数值相同；改权重后仍会除以 `sum()`。）

## 标量广播 Series（zscore 退化分支）

`zscore` 在标准差为 0 或 `NaN` 时，返回与输入 **同 index** 的全 0 序列：

| 用法 | 说明 |
|------|------|
| `pd.Series(0, index=series.index)` | 标量 `0` 按 index 广播成 Series |

**输入代码**：

```python
flat = pd.Series({"510880.SH": 1.0, "159915.SZ": 1.0, "513100.SH": 1.0})
zeros = pd.Series(0, index=flat.index)
```

**输出结果**：

```text
pd.Series(0, index=...) -> {'510880.SH': 0, '159915.SZ': 0, '513100.SH': 0}
```

## 空 Series 填分 + idxmax（1_ETF轮动）

`1_1_ETF轮动_选.py` 第 65 行：先建 **四格空积分榜**，内层循环按 ETF 代码填分，再用 `idxmax()` 选当日持仓。

| 用法 | 说明 |
|------|------|
| `pd.Series(index=etf_libs, dtype='float64')` | 只指定 **index**（四只 ETF 代码），值先为 `NaN`；`dtype` 声明格子存浮点分 |
| `scores[stk] = ...` | 按代码写入该只 ETF 的得分（与 `dict[stk]=` 相同写法） |
| `scores.idxmax()` | 返回 **分数最大** 对应的 index（即 ETF 代码）；并列时取 index 里 **第一个** 最大值 |
| `scores.sort_values(ascending=False)` | 调试时按分从高到低查看 |

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

- `DataFrame` 更像二维表：行索引常是日期或标的代码，列名常是字段名，如 `close`、`bias`、`hold`。
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

## 空 DataFrame 预建因子表（13_ETF轮动_v3 · factor_df）

三脚本每日（或单次）算分前，先建 **4 行 × 3 列** 空表，再逐 ETF 填因子原始值。

| 用法 | 说明 |
|------|------|
| `pd.DataFrame(index=etf_libs, columns=[...], dtype='float64')` | 行 index = ETF 代码，列 = 因子名；初值 `NaN` |
| `factor_df.at[stk, 'bias'] = ...` | 按 **行标签 + 列名** 写单个标量（比 `loc` 更适合单格赋值） |
| `factor_df.apply(zscore, axis=0)` | **按列**做 Z-Score；每列跨 4 只 ETF 标准化 |
| `history['close']` | 从行情表取单列 → `Series`，传入 `bias_momentum` / `slope_momentum` |
| `efficiency_momentum(history)` | 入参为 **DataFrame**（需 `open/high/low/close` 四列） |

**输入代码**：

```python
etf_libs = ["510880.SH", "159915.SZ", "513100.SH", "518880.SH"]
factor_df = pd.DataFrame(index=etf_libs, columns=["bias", "slope", "efficiency"], dtype="float64")
factor_df.at["513100.SH", "bias"] = 45.6
# ... 其余格子同理
z_factors = factor_df.apply(zscore, axis=0)
```

**输出结果**：

```text
factor_df:
            bias  slope  efficiency
510880.SH  12.3    1.2         0.5
159915.SZ   8.1    0.8         0.3
513100.SH  45.6    2.1         1.1
518880.SH   3.2    0.5         0.2
z_factors.apply(zscore, axis=0) columns -> ['bias', 'slope', 'efficiency']
z_factors index -> ['510880.SH', '159915.SZ', '513100.SH', '518880.SH']
```

现场数据流见 [`13_ETF轮动_v3/DATAFLOW.md`](../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md) 第二步因子表。

## 行情列裁剪 + reset_index(drop=True)（13_ETF轮动_v3 · df_all）

`1_1` 下载行情后只留 OHLC，并 **丢掉日期 index**，改行号为 `0, 1, 2, …`，与外层 `enumerate(trade_days)` 的 `idx` 对齐。

| 用法 | 说明 |
|------|------|
| `df[['open', 'high', 'low', 'close']]` | **双中括号**取多列 → 仍是 `DataFrame` |
| `.reset_index(drop=True)` | 原 index 不保留为列；新 index 为 `0…n-1` |
| `df_all = {}` + `df_all[stk] = ...` | 外层是标准库 **dict**；值才是 `DataFrame` |

**输入代码**：

```python
bars = pd.DataFrame({...}, index=["20240102", "20240103", "20240105"])  # 含 vol 等列
trimmed = bars[["open", "high", "low", "close"]].reset_index(drop=True)
```

**输出结果**：

```text
trimmed.columns -> ['open', 'high', 'low', 'close']
trimmed.index -> [0, 1, 2]
trimmed.shape -> (3, 4)
```

**注意点**：`generate_stock_selection.py` **未** `reset_index`，保留日期 index；与 `1_1` 的 `iloc[:idx]` 对齐方式不同，见 [11-etf-v3-hkcodex](11-etf-v3-hkcodex.md)。`reset_index` 细节见 [02-pandas-readwrite-index](02-pandas-readwrite-index.md)。

## 取列当 Series + iloc 取单元格（13_ETF轮动_v3 · 日历）

| 用法 | 说明 |
|------|------|
| `df['cal_date']` | 取单列 → `Series`（与 `df['score']` 同型） |
| `df['cal_date'].tolist()` | 转成 Python 列表，供 `enumerate` |
| `df.iloc[0]['cal_date']` | 第 0 行、`cal_date` 列的标量（如回推 `start_date`） |
| `enumerate(trade_days_with_warmup['cal_date'])` | `idx` 与 `df_all[stk].iloc[:idx]` 配套 |

**输入代码**：

```python
trade_days = pd.DataFrame({"cal_date": ["20231227", "20231228", "20240102"], ...})
start_date = trade_days.iloc[0]["cal_date"]
cal_dates = trade_days["cal_date"].tolist()
```

**输出结果**：

```text
start_date -> 20231227
trade_days['cal_date'].tolist() -> ['20231227', '20231228', '20240102']
type(trade_days['cal_date']) -> Series
```

`history = df_all[stk].iloc[:idx]` 的切片语义见 [03-pandas-loc-iloc-filter-sort](03-pandas-loc-iloc-filter-sort.md)。

## Z-Score 加权融合 → combined_scores（13_ETF轮动_v3）

因子表标准化后，与 `weights` 按列对齐相乘，再按行求和，得到 **每只 ETF 一个分** 的 `Series`（index = ETF 代码）。

| 用法 | 说明 |
|------|------|
| `z_factors.mul(weights, axis=1)` | 每行 ETF × 各列因子权重；`weights` 的 index 须与列名一致 |
| `.sum(axis=1)` | 按行求和 → `Series`，index 仍为 ETF 代码 |
| `.sort_values(ascending=False)` | 分数从高到低；**v3 用 `index[0]` 取最高**，不用 `idxmax` |
| `.index[0]` / `.iloc[0]` | 排序后第一名：标签 vs 位置（并列时 `index[0]` 取稳定排序第一个） |
| `.get(current_hold, np.nan)` | 查昨日持仓得分；不在榜则 `NaN` |
| `.dropna()` | 仅 `generate_stock_selection`：去掉因子算不出的 ETF 后再排序 |

**输入代码**：

```python
combined_scores = z_factors.mul(weights, axis=1).sum(axis=1)
combined_scores = combined_scores.sort_values(ascending=False)
top_candidate = combined_scores.index[0]
top_score = combined_scores.iloc[0]
current_score = combined_scores.get("159915.SZ", np.nan)
```

**输出结果**：

```text
combined_scores:
 513100.SH    1.636762
510880.SH   -0.070940
159915.SZ   -0.607135
518880.SH   -0.958687
top_candidate -> 513100.SH
top_score -> 1.6367623255175467
combined_scores.get(current_hold, nan) -> -0.6071352951411324
dropna 后 index -> ['513100.SH', '159915.SZ', '518880.SH']
```

**v1 vs v3 选股容器**：`1_ETF轮动` 用空 `Series` + `idxmax()`；v3 用 `factor_df` → `combined_scores` + `sort_values` + `index[0]`。

## 回测台账空表（1_2_ETF轮动_回测 · g.df）

| 用法 | 说明 |
|------|------|
| `pd.DataFrame(index=trade_day['cal_date'], columns=col_names)` | 行 = 每个交易日，列 = 持仓/现金/净值字段；初值 `NaN` |
| `g.df.loc[dt_str, 'cash'] = ...` | 策略 `next` 里按日回填（见 [03 · loc](03-pandas-loc-iloc-filter-sort.md)） |
| `g.df.to_csv(...)` | 写出 `ETF轮动_v3_portfolio.csv`（见 [02 · to_csv](02-pandas-readwrite-index.md)） |

**输入代码**：

```python
col_names = ["hold1", "vol1", "close1", "cash", "value", "value_cal"]
portfolio_df = pd.DataFrame(index=trade_days["cal_date"], columns=col_names)
portfolio_df.loc["20240102", "cash"] = 100000.0
portfolio_df.loc["20240102", "hold1"] = "513100.SH"
```

**输出结果**：

```text
portfolio_df.loc['20240102'].to_dict() -> {'hold1': '513100.SH', 'vol1': nan, 'close1': nan, 'cash': 100000.0, 'value': nan, 'value_cal': nan}
```

## dict 分析结果 → Series（1_2 · pnl）

Backtrader `TimeReturn` 分析器返回 `dict`（日期 → 收益率），包一层即带日期 index 的 `Series`：

| 用法 | 说明 |
|------|------|
| `pd.Series(analyzer.get_analysis())` | dict 的 key 成为 index |
| `hx.analyzer(pnl, benchmark, ...)` | 下游接口吃此 `Series`（见 [11-etf-v3-hkcodex](11-etf-v3-hkcodex.md)） |

**输入代码**：

```python
pnl = pd.Series({"20240102": 0.001, "20240103": -0.002, "20240105": 0.0005})
```

**输出结果**：

```text
pnl:
 20240102    0.0010
20240103   -0.0020
20240105    0.0005
pnl.index -> ['20240102', '20240103', '20240105']
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

## v3 三脚本 · Series / DataFrame 速查

| 变量 / 动作 | 类型 | 脚本 |
|-------------|------|------|
| `weights` | `Series`（index=因子名） | `1_1`、`generate` |
| `factor_df` | `DataFrame`（index=ETF，列=因子） | 三脚本算分段 |
| `z_factors` | `DataFrame`（同形） | `apply(zscore, axis=0)` |
| `combined_scores` | `Series`（index=ETF） | 三脚本 |
| `df_all[stk]` | `DataFrame`（OHLC） | 三脚本；`reset_index` 仅 `1_1` |
| `trade_days_with_warmup['cal_date']` | `Series` | `1_1`、`generate` |
| `g.df` | `DataFrame`（台账） | 仅 `1_2` |
| `pnl` | `Series`（index=日期） | 仅 `1_2` |

完整数据流：[13_ETF轮动_v3/DATAFLOW.md](../../../Quant/HKCodex/HKCodex-CodeSets_v3/13_ETF轮动_v3/DATAFLOW.md)

## 官方文档

- [pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)  
- [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
