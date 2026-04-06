"""对应 03-math-rounding.md：math 取整、round、decimal"""

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


if __name__ == "__main__":
    main()
