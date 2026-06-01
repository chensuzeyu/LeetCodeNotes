# Python 3 速查 · 量化代码阅读

**与刷题 / 日常开发分离**：本分册聚焦 `D:\develop\Quant` 里最常碰到的 `pandas`、`numpy`、`backtrader`、`hkcodex`，目标是降低你阅读 `1_ETF轮动` 这类脚本的门槛，而不是做完整数据科学教材。

目标：**覆盖量化脚本最常见的数据结构、索引操作、回测对象模型与本地接口调用**，优先服务“看懂输入、输出、路径、日期和数据流”。运行前默认已执行 **`conda activate hkcodex`**，并使用 **Python 3.9.x**。

## 怎么用

```bash
cd python-core-quickref/quant/scripts
python3 run_all.py
```

或单课：`python3 04_pandas_datetime_ffill_shape.py`

要求：**`pandas` / `numpy` / `backtrader` / `hkcodex` 已可导入**。本册不做缺包兜底，默认在本地 `hkcodex` Conda 环境中运行。

## 文档索引

| 文档 | 演示脚本 | 内容 |
|------|----------|------|
| [01-pandas-series-dataframe.md](01-pandas-series-dataframe.md) | [scripts/01_pandas_series_dataframe.py](scripts/01_pandas_series_dataframe.py) | `Series`、`DataFrame`、列与索引 |
| [02-pandas-readwrite-index.md](02-pandas-readwrite-index.md) | [scripts/02_pandas_readwrite_index.py](scripts/02_pandas_readwrite_index.py) | `read_csv`、`to_csv`、`index_col`、`set_index`、`reset_index` |
| [03-pandas-loc-iloc-filter-sort.md](03-pandas-loc-iloc-filter-sort.md) | [scripts/03_pandas_loc_iloc_filter_sort.py](scripts/03_pandas_loc_iloc_filter_sort.py) | `[]`、`.loc`、`.iloc`、筛选、排序、去重 |
| [04-pandas-datetime-ffill-shape.md](04-pandas-datetime-ffill-shape.md) | [scripts/04_pandas_datetime_ffill_shape.py](scripts/04_pandas_datetime_ffill_shape.py) | `to_datetime`、`DatetimeIndex`、`strftime`、`ffill` |
| [05-numpy-array-math.md](05-numpy-array-math.md) | [scripts/05_numpy_array_math.py](scripts/05_numpy_array_math.py) | `array`、`arange`、广播、`log`、`exp`、`mean`、`var`、`where` |
| [06-numpy-polyfit-score.md](06-numpy-polyfit-score.md) | [scripts/06_numpy_polyfit_score.py](scripts/06_numpy_polyfit_score.py) | `polyfit`、拟合值、`r_squared`、ETF 动量打分 |
| [07-backtrader-cerebro-data-strategy.md](07-backtrader-cerebro-data-strategy.md) | [scripts/07_backtrader_cerebro_data_strategy.py](scripts/07_backtrader_cerebro_data_strategy.py) | `PandasData`、`Cerebro`、`Strategy`、`next` |
| [08-backtrader-order-broker-analyzer.md](08-backtrader-order-broker-analyzer.md) | [scripts/08_backtrader_order_broker_analyzer.py](scripts/08_backtrader_order_broker_analyzer.py) | 下单、broker、`notify_order`、`notify_trade`、`TimeReturn` |
| [09-hkcodex-dates-marketdata.md](09-hkcodex-dates-marketdata.md) | [scripts/09_hkcodex_dates_marketdata.py](scripts/09_hkcodex_dates_marketdata.py) | `get_trade_days`、`fund_daily`、`index_daily` |
| [10-1etf-chain.md](10-1etf-chain.md) | [scripts/10_1etf_chain.py](scripts/10_1etf_chain.py) | `1_ETF轮动` 的 `txt` 链路、`portfolio.csv` 与 `cwd` |
| [11-etf-v3-hkcodex.md](11-etf-v3-hkcodex.md) | [scripts/11_etf_v3_hkcodex.py](scripts/11_etf_v3_hkcodex.py) | `13_ETF轮动_v3` 全部 hkcodex 用法（三脚本对照） |

## 策略现场手册（数据流）

完整数据流、缓存路径、变量对齐见 HKCodex 策略目录下的 **`DATAFLOW.md`**。本仓索引：

- [strategies/README.md](strategies/README.md) — 多策略总表  
- [strategies/01-ETF轮动.md](strategies/01-ETF轮动.md) — `1_ETF轮动` 先修课 + 链接  
- [strategies/13-ETF轮动_v3.md](strategies/13-ETF轮动_v3.md) — `13_ETF轮动_v3` 先修课 + 链接  

读 `1_ETF轮动` 最低路径：`01`～`06` + `09` + `10` + 上述 **DATAFLOW**。  
读 `13_ETF轮动_v3` 在同样基础上加 **`11`**（hkcodex 三脚本对照）+ **v3 DATAFLOW**。

## 学习顺序

`01` → `02` → `03` → `04` → `05` → `06` → `07` → `08` → `09` → `10` → `11`

读 `1_ETF轮动` 的最低顺序建议是：`01`～`06` + `09` + `10`；做回测细读再加 `07`、`08`。  
读 `13_ETF轮动_v3` 时在第 9 课后加 `11`。

## 编写规范

- 各课 Markdown 是对应脚本的说明层，默认以“**输入代码 / 输出结果**”组织内容。
- 表格是脚本可验证清单，不是概念清单；表格中写到的用法，必须能在对应脚本里找到真实演示。
- 若文档已点名参数口径、返回类型、返回形状、默认行为或常见空结果分支，脚本至少要覆盖高频分支；不适合稳定演示的部分需明确写成说明性文字。
- 每个知识点默认包含：
  - **输入代码**：与脚本变量、参数、调用一致。
  - **输出结果**：来自当前脚本真实运行结果。
  - **注意点**：仅在容易踩坑时补充。
- `pandas` / `numpy` / `backtrader` 章节优先使用自造小数据，保证输出稳定、例子能手算。
- `hkcodex` 章节使用固定历史区间，只打印少量字段或片段，避免整段动态行情污染文档。
- 本册允许对少量环境敏感片段做占位规范化，常用占位符：
  - `<TMP_PATH>`
  - `<CWD>`
  - `<PY_VERSION>`
  - `<HKCODEX_HELPER>`

## 维护

- 新增量化向主题：先补 `scripts/0x_*.py`，再写 `0x-*.md`，最后更新 `scripts/run_all.py`。
- 各课 Markdown 中的「输入代码 / 输出结果」应与当前脚本保持一致；改了脚本请同步更新文档。
- 文档与脚本的总约定见 [上层 README.md](../README.md)。
