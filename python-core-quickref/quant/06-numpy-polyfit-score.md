# 06 · numpy 的 polyfit 与动量打分

完整演示：[scripts/06_numpy_polyfit_score.py](scripts/06_numpy_polyfit_score.py)  
运行：`python3 06_numpy_polyfit_score.py`

偏**`1_ETF轮动` 里最关键的一段数值逻辑**：取对数、线性拟合、算斜率、算 `r_squared`、最后乘成分数。  
你现在不必先把统计学吃透，但至少要能顺着变量看懂这段数据流。

## `np.polyfit`

| 用法 | 说明 |
|------|------|
| `np.polyfit(x, y, 1)` | 一次直线拟合，返回斜率和截距 |
| `x = np.arange(y.size)` | 给价格序列配一个等间距横轴 |

- 这里用 `log(close)` 再拟合，是为了把“复利增长”近似转成线性斜率来观察。

**输入代码**：

```python
close = np.array([100.0, 101.0, 103.0, 106.0, 108.0])
y = np.log(close)
x = np.arange(y.size)
slope, intercept = np.polyfit(x, y, 1)
```

**输出结果**：

```text
close -> [100.0, 101.0, 103.0, 106.0, 108.0]
x -> [0, 1, 2, 3, 4]
log(close) -> [4.60517, 4.615121, 4.634729, 4.663439, 4.682131]
slope = 0.020224  intercept = 4.59967
```

## 拟合值 / `r_squared`

| 用法 | 说明 |
|------|------|
| `fitted = slope * x + intercept` | 直线拟合值 |
| `r_squared` | 近似衡量“这段趋势有多直” |

- `r_squared` 越接近 1，说明点越贴近这条拟合直线；越小说明走势越“弯”或噪声越大。

**输入代码**：

```python
fitted = slope * x + intercept
r_squared = 1 - (np.sum((y - fitted) ** 2) / ((len(y) - 1) * np.var(y, ddof=1)))
```

**输出结果**：

```text
fitted -> [4.59967, 4.619894, 4.640118, 4.660342, 4.680566]
r_squared -> 0.977506
```

## 按 `1_ETF轮动` 风格算分

| 用法 | 说明 |
|------|------|
| `math.pow(math.exp(slope), 250) - 1` | 把日斜率近似年化 |
| `annualized_returns * r_squared` | 得到最终分数 |

- 这个分数本质上是在平衡“涨得快”和“走势直不直”两件事。

**输入代码**：

```python
annualized_returns = math.pow(math.exp(slope), 250) - 1
score = annualized_returns * r_squared
```

**输出结果**：

```text
annualized_returns -> 155.964001
score -> 152.455708
```

**注意点**：这里的年化值会很夸张，因为我们故意用了很短、单边上涨的小样本；重点是理解公式和变量流，不是把这个数当真实策略收益。

## 官方文档

- [numpy.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
