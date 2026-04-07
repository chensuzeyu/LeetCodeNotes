"""对应 07-chr-bitwise.md：ord/chr、位运算"""

from __future__ import annotations

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("ord / chr")
    print("ord('A') =", ord("A"), " chr(65) =", chr(65))
    print("ord('你') =", ord("你"))

    section("str 字符类判断（节选）")
    print("'9'.isdigit() =", "9".isdigit(), "  'a'.isalpha() =", "a".isalpha())

    section("按位与或非、异或、移位")
    a, b = 0b1100, 0b1010
    print(f"a={a:#06b} b={b:#06b}")
    print(f"a&b = {a & b:#06b}", f"a|b = {a | b:#06b}", f"a^b = {a ^ b:#06b}")
    print("~a =", ~a)
    print("a << 1 =", a << 1, bin(a << 1), " a >> 1 =", a >> 1, bin(a >> 1))

    section("lowbit / 去掉最低 1")
    n = 0b1011000
    low = n & -n
    print(f"n={n:#b} lowbit n&-n = {low:#b}")
    print(f"n&(n-1) 去掉最低位1 -> {n & (n - 1):#b}")

    section("二进制中 1 的个数")
    x11 = 0b1011
    portable = bin(x11).count("1")
    print(f"popcount(0b1011) = {portable}（写法: bin(n).count('1')）", end="")
    if hasattr(x11, "bit_count"):
        print(f" ；int.bit_count() = {x11.bit_count()}")
    else:
        print("（高版本 Python 也可用 int.bit_count()）")

    section("子集枚举：掩码与下标")
    items = ["a", "b", "c"]
    n_items = len(items)
    for mask in range(1 << n_items):
        chosen = [items[i] for i in range(n_items) if mask >> i & 1]
        if mask <= 4:
            print(f"mask={mask:#04b} ->", chosen)


if __name__ == "__main__":
    main()
