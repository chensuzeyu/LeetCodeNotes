# 03 · math：取整、数论小表、decimal

完整演示：[scripts/03_math_rounding.py](scripts/03_math_rounding.py)  
运行：`python3 03_math_rounding.py`

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## 速查 · 取整与 round

| 需求 | 用法 |
|------|------|
| 向下取整 | `math.floor(x)` |
| 向上取整 | `math.ceil(x)` |
| 向 0 截断 | `math.trunc(x)` 或 `int(x)`（`x` 为 float） |
| 就近（注意 `.5`） | `round(x)` / `round(x, ndigits)`：Python 3 对 `.5` 为银行家舍入（凑偶） |
| 金额 / 精确小数 | `decimal.Decimal` + `quantize` + `ROUND_HALF_UP` 等 |

### `floor` / `ceil` / `trunc` / `int`

- **`int(x)`**（float）：向 0 截断。
- **`math.floor(x)`**：向负无穷取整；负数时常与 `int` 不同。
- 对已经是整数值的数，`floor` / `ceil` / `trunc` 结果会一致；差异主要出现在带小数部分时。

**输入代码**：

```python
x = 2.7
y = -2.7

math.floor(x), math.ceil(x), math.trunc(x), int(x)
math.floor(y), math.ceil(y), math.trunc(y), int(y)
```

**输出结果**：

```text
x = 2.7  floor=2 ceil=3 trunc=2 int=2
y = -2.7 floor=-3 ceil=-2 trunc=-2 int=-2
int(-2.7) != floor(-2.7)：向 0 vs 向 -∞
```

### `round(x)` 与 `round(x, ndigits)`

- Python 3 的 `round` 在 `.5` 上按银行家舍入，不是始终“见 5 进 1”。

**输入代码**：

```python
for v in [2.5, 3.5, 4.5, -2.5]:
    round(v)

round(12.3456, 2)
round(12.3456, 3)
round(2.675, 2)
```

**输出结果**：

```text
round(2.5) = 2
round(3.5) = 4
round(4.5) = 4
round(-2.5) = -2
round(12.3456, 2) = 12.35  round(12.3456, 3) = 12.346
round(2.675, 2) = 2.67 （float 二进制表示会影响结果）
```

需要“0.5 一律进位”这类业务规则时，用 **`Decimal`**，不要硬套 `round()`。

## 速查 · 数论（刷题高频）

环境按本仓库 **Python 3.9+**；`lcm` / `comb` / `perm` / `isqrt` 等均可直接使用。

| 需求 | 用法 |
|------|------|
| 最大公约数 | `math.gcd(a, b)` |
| 最小公倍数 | `math.lcm(a, b)` |
| 模幂 \(a^b \bmod m\) | `pow(a, b, m)`，不要用 `math.pow` |
| 整数平方根 \(\lfloor\sqrt{n}\rfloor\) | `math.isqrt(n)` |
| 组合 / 排列数 | `math.comb(n, k)`、`math.perm(n, k)` |
| 阶乘 | `math.factorial(n)` |

### `gcd` / `lcm` / `pow(..., mod)` / `isqrt` / `comb` / `perm` / `factorial`

- `pow(a, b, m)` 是**内置函数**的三参数版本，效率和语义都比先算 `a ** b` 再 `% m` 更合适。
- `isqrt(n)` 返回的是整数平方根，不会像 `sqrt` 那样先进入浮点数世界。

**输入代码**：

```python
math.gcd(54, 24)
math.lcm(12, 18)
pow(7, 1000, 10**9 + 7)
math.isqrt(17)
math.comb(5, 2)
math.perm(5, 2)
math.factorial(6)
```

**输出结果**：

```text
gcd(54, 24) = 6
lcm(12, 18) = 36
pow(7, 1000, 1000000007) = 224787023  （三参数内置，模幂）
isqrt(17) = 4  （floor(sqrt(n))）
comb(5, 2) = 10  perm(5, 2) = 20
factorial(6) = 720
```

## Decimal（精确小数）

- 用字符串构造 `Decimal("2.675")`，避免先经历 `float` 的二进制误差。
- `quantize` + `ROUND_HALF_UP` 可实现“见 5 进一位”这类规则。

### `Decimal` 与 `quantize`

- `Decimal("2.675")` 这种**字符串构造**最稳；`Decimal(2.675)` 会把 float 误差原样带进来。

**输入代码**：

```python
u = Decimal("2.5")
u.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

v2 = Decimal("2.675")
v2.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
Decimal(2.675), Decimal("2.675")
```

**输出结果**：

```text
Decimal("2.5").quantize(..., ROUND_HALF_UP) -> 3 -> int -> 3
Decimal("2.675").quantize(Decimal("0.01"), ROUND_HALF_UP) -> 2.68 （应用字符串构造，避免 float 二进制误差）
Decimal(2.675) 与 Decimal("2.675") 不同 -> 2.67499999999999982236431605997495353221893310546875 vs 2.675
```

## 官方文档

- [math](https://docs.python.org/3/library/math.html)  
- [decimal](https://docs.python.org/3/library/decimal.html)
