# 03 · math：取整、数论小表、decimal

完整演示：`scripts/03_math_rounding.py`  
运行：`python 03_math_rounding.py`

## 速查 · 取整与 round

| 需求 | 用法 |
|------|------|
| 向下取整 | `math.floor(x)` |
| 向上取整 | `math.ceil(x)` |
| 向 0 截断 | `math.trunc(x)` 或 `int(x)`（`x` 为 float） |
| 就近（注意 `.5`） | `round(x)` / `round(x, ndigits)`：Python 3 对 `.5` 为**银行家舍入（凑偶）**，不一定是「小学四舍五入」 |
| 金额 / 精确小数 | `decimal.Decimal` + `quantize` + `ROUND_HALF_UP` 等 |

## 速查 · 数论（刷题高频）

环境按本仓库 **Python 3.9+**；`lcm` / `comb` / `perm` / `isqrt` 等为当前常用内置能力。

| 需求 | 用法 |
|------|------|
| 最大公约数 | `math.gcd(a, b)`；扩展欧几里得需手写 |
| 最小公倍数 | `math.lcm(a, b)`（多参数可递推：`math.lcm(a, math.lcm(b, c))`） |
| 模幂 \(a^b \bmod m\) | **内置** `pow(a, b, m)`，大数场景优先用它（`math.pow` 是 float，不要用） |
| 整数平方根 \(\lfloor\sqrt{n}\rfloor\) | `math.isqrt(n)`，`n` 须为非负 `int` |
| 组合 / 排列数 | `math.comb(n, k)`、`math.perm(n, k)`（定义见文档；`k>n` 时 `comb` 为 0） |
| 阶乘 | `math.factorial(n)`（`n` 较大时注意指数级增长，题目常需取模改写） |

## 易混点

- `int(-2.7)` 与 `math.floor(-2.7)`：**不相同**（一个向 0，一个向负无穷）。  
- 需要「0.5 一律进位」这类规则时，不要依赖 `round()`，用 `decimal` 模块。  
- `math.pow` 返回 **float**；要**整数模幂**只用 **`pow(a, b, m)`**。

## 官方文档

- [math](https://docs.python.org/3/library/math.html)  
- [decimal](https://docs.python.org/3/library/decimal.html)
