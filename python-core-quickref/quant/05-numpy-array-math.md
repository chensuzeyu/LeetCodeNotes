# 05 · numpy 的 array / 广播 / 常见数学函数

完整演示：[scripts/05_numpy_array_math.py](scripts/05_numpy_array_math.py)  
运行：`python3 05_numpy_array_math.py`

偏**量化里最常见的数值基础动作**：向量化计算、取对数、还原指数、条件分支、均值和方差。  
下文全部用很小的可手算例子，先把直觉建立起来。

## `array` / `arange` / 广播

| 用法 | 说明 |
|------|------|
| `np.array([...])` | 构造数组 |
| `np.arange(n)` | 生成 `0..n-1` |
| 广播 | 一个标量或同长度数组自动作用到整列数据 |

**输入代码**：

```python
a = np.array([1.0, 2.0, 3.0])
b = np.arange(3)
a + 10
a * np.array([1, 10, 100])
```

**输出结果**：

```text
a -> [1.0, 2.0, 3.0]
np.arange(3) -> [0, 1, 2]
a + 10 -> [11.0, 12.0, 13.0]
a * np.array([1, 10, 100]) -> [1.0, 20.0, 300.0]
```

## `log` / `exp` / `where`

| 用法 | 说明 |
|------|------|
| `np.log(x)` | 自然对数 |
| `np.exp(x)` | 指数 |
| `np.where(cond, a, b)` | 条件分支 |

**输入代码**：

```python
x = np.array([1.0, np.e, np.e ** 2])
np.log(x)
np.exp(np.array([0.0, 1.0, 2.0]))
np.where(a > 1.5, "high", "low")
```

**输出结果**：

```text
np.log([1, e, e^2]) -> [0.0, 1.0, 2.0]
np.exp([0, 1, 2]) -> [1.0, 2.718282, 7.389056]
np.where(a > 1.5, 'high', 'low') -> ['low', 'high', 'high']
```

## `mean` / `var`

| 用法 | 说明 |
|------|------|
| `np.mean(scores)` | 均值 |
| `np.var(scores, ddof=1)` | 样本方差 |

**输入代码**：

```python
scores = np.array([0.9, 1.1, 1.0, 1.2])
np.mean(scores)
np.var(scores, ddof=1)
```

**输出结果**：

```text
scores -> [0.9, 1.1, 1.0, 1.2]
np.mean(scores) -> 1.05
np.var(scores, ddof=1) -> 0.016667
```

## 官方文档

- [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)  
- [numpy.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)  
- [numpy.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
