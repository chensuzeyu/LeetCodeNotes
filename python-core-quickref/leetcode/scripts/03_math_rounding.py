"""对应 03-math-rounding.md：math 取整、数论小表、round、decimal"""

from __future__ import annotations

import math
from decimal import Decimal, ROUND_HALF_UP

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("math.floor / ceil / trunc 与 int(x)【向 0 截断】")
    x = 2.7
    y = -2.7
    print(f"x = {x}  floor={math.floor(x)} ceil={math.ceil(x)} trunc={math.trunc(x)} int={int(x)}")
    print(f"y = {y} floor={math.floor(y)} ceil={math.ceil(y)} trunc={math.trunc(y)} int={int(y)}")
    print("int(-2.7) != floor(-2.7)：向 0 vs 向 -∞")

    section("round(x)：Python3 银行家舍入（.5 凑偶）；非「小学四舍五入」")
    for v in [2.5, 3.5, 4.5, -2.5]:
        print(f"round({v}) = {round(v)}")

    v = 12.3456
    print(f"round({v}, 2) = {round(v, 2)}  round({v}, 3) = {round(v, 3)}")
    print("round(2.675, 2) =", round(2.675, 2), "（float 二进制表示会影响结果）")

    section("数论：gcd / lcm / pow(a,b,m) / isqrt / comb / perm / factorial")
    a, b, m = 54, 24, 10**9 + 7
    print(f"gcd({a}, {b}) = {math.gcd(a, b)}")
    print(f"lcm(12, 18) = {math.lcm(12, 18)}")
    print(f"pow(7, 1000, {m}) = {pow(7, 1000, m)}  （三参数内置，模幂）")
    n = 17
    print(f"isqrt({n}) = {math.isqrt(n)}  （floor(sqrt(n))）")
    print(f"comb(5, 2) = {math.comb(5, 2)}  perm(5, 2) = {math.perm(5, 2)}")
    print(f"factorial(6) = {math.factorial(6)}")

    section("Decimal：精确表示 + quantize + ROUND_HALF_UP【见 5 进一位】")
    u = Decimal("2.5")
    q = u.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    print(f'Decimal("2.5").quantize(..., ROUND_HALF_UP) -> {q} -> int -> {int(q)}')
    v2 = Decimal("2.675")
    print(
        f'Decimal("2.675").quantize(Decimal("0.01"), ROUND_HALF_UP) ->',
        v2.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "（应用字符串构造，避免 float 二进制误差）",
    )
    print(
        "Decimal(2.675) 与 Decimal('2.675') 不同 ->",
        Decimal(2.675),
        "vs",
        Decimal("2.675"),
    )


if __name__ == "__main__":
    main()
