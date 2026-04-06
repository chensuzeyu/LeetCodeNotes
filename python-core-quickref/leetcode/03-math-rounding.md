# 03 · 取整与舍入（math / round / decimal）

完整演示：`scripts/03_math_rounding.py`  
运行：`python 03_math_rounding.py`

## 速查

| 需求 | 用法 |
|------|------|
| 向下取整 | `math.floor(x)` |
| 向上取整 | `math.ceil(x)` |
| 向 0 截断 | `math.trunc(x)` 或 `int(x)`（`x` 为 float） |
| 就近（注意 `.5`） | `round(x)` / `round(x, ndigits)`：Python 3 对 `.5` 为**银行家舍入（凑偶）**，不一定是「小学四舍五入」 |
| 金额 / 精确小数 | `decimal.Decimal` + `quantize` + `ROUND_HALF_UP` 等 |

## 易混点

- `int(-2.7)` 与 `math.floor(-2.7)`：**不相同**（一个向 0，一个向负无穷）。  
- 需要「0.5 一律进位」这类规则时，不要依赖 `round()`，用 `decimal` 模块。

## 官方文档

- [math](https://docs.python.org/3/library/math.html)  
- [decimal](https://docs.python.org/3/library/decimal.html)
