# 03 · math：取整、数论小表、decimal

完整演示：[scripts/03_math_rounding.py](scripts/03_math_rounding.py)  
运行：`python 03_math_rounding.py`

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## 速查 · 取整与 round

| 需求 | 用法 |
|------|------|
| 向下取整 | `math.floor(x)` |
| 向上取整 | `math.ceil(x)` |
| 向 0 截断 | `math.trunc(x)` 或 `int(x)`（`x` 为 float） |
| 就近（注意 `.5`） | `round(x)` / `round(x, ndigits)`：Python 3 对 `.5` 为**银行家舍入（凑偶）**，不一定是「小学四舍五入」 |
| 金额 / 精确小数 | `decimal.Decimal` + `quantize` + `ROUND_HALF_UP` 等 |

### `floor` / `ceil` / `trunc` / `int`（负数）

- **`int(x)`**（float）：向 **0** 截断。
- **`math.floor(x)`**：向 **负无穷** 取整；对负数与 `int` **不同**。

**预期输出摘录**：

```text
x = 2.7  floor=2 ceil=3 trunc=2 int=2
y = -2.7 floor=-3 ceil=-2 trunc=-2 int=-2
int(-2.7) != floor(-2.7)：向 0 vs 向 -∞
```

### `round` 与「四舍五入」

- Python 3 的 `round` 在 `.5` 上按**银行家舍入（凑偶）**，不要当成始终进位。

**预期输出摘录**：

```text
round(2.5) = 2
round(3.5) = 4
round(4.5) = 4
round(-2.5) = -2
round(12.3456, 2) = 12.35  round(12.3456, 3) = 12.346
```

需要「0.5 一律进位」等规则时，用 **`Decimal`**（见下）而非依赖 `round()`。

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

### `pow(a, b, m)` 与 `math.pow`

- **整数模幂**：只用三参数 **`pow(a, b, m)`**。
- **`math.pow`**：返回 **float**，不适合大整数取模。

**预期输出摘录**：

```text
pow(7, 1000, 1000000007) = 224787023  （三参数内置，模幂）
isqrt(17) = 4  （floor(sqrt(n))）
comb(5, 2) = 10  perm(5, 2) = 20
```

## Decimal（精确小数）

- 用 **字符串**构造 `Decimal("2.675")`，避免先转 `float` 再进 `Decimal` 引入二进制误差。
- **`quantize` + `ROUND_HALF_UP`**：可按业务规则做「见 5 进一位」等。

**预期输出摘录**：

```text
Decimal("2.5").quantize(..., ROUND_HALF_UP) -> 3 -> int -> 3
Decimal("2.675").quantize(Decimal("0.01"), ROUND_HALF_UP) -> 2.68 （应用字符串构造，避免 float 二进制误差）
```

## 官方文档

- [math](https://docs.python.org/3/library/math.html)  
- [decimal](https://docs.python.org/3/library/decimal.html)
