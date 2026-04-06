"""对应 02-containers.md：list / dict / str / set 常用方法"""

from __future__ import annotations

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("list：append / pop / insert / 切片 / 反转切片")
    nums = [1, 2, 3]
    nums.append(4)
    print("append(4) ->", nums)
    last = nums.pop()
    print("pop() ->", last, " nums ->", nums)
    nums.insert(0, 9)
    print("insert(0, 9) ->", nums)
    mid = nums.pop(1)
    print("pop(1) ->", mid, " nums ->", nums)
    print("nums[1:3]（左闭右开）->", nums[1:3])
    print("nums[::-1]（新序列，原列表不变）->", nums[::-1], " nums 仍为", nums)

    section("dict：[] / KeyError / get / setdefault / in / items")
    d: dict[str, int] = {"a": 1}
    print("d =", d)
    print("d['a'] =", d["a"])
    try:
        _ = d["missing"]
    except KeyError as e:
        print("d['missing'] -> KeyError:", e)
    print("d.get('b', 0) =", d.get("b", 0))
    d.setdefault("b", 2)
    print("setdefault('b', 2) 后 d =", d)
    print("'a' in d =", "a" in d, "  'z' in d =", "z" in d)
    for k, v in d.items():
        print(f"  item: {k!r} -> {v}")

    section("str：split（默认空白 / 指定分隔符）/ strip / 切片")
    s = "  a,b, c  \n"
    print("原字符串 repr:", repr(s))
    print("split()（任意空白）->", "hello   world\nfoo".split())
    print("split(',') ->", s.split(","))
    print("strip() -> repr:", repr(s.strip()))
    print(repr("  abc\n") + ".lstrip() ->", repr("  abc\n".lstrip()))
    print(repr("abc  \n") + ".rstrip() ->", repr("abc  \n".rstrip()))
    print("'hello'[1:4]（左闭右开）->", "hello"[1:4])

    section("set：add / remove / discard；交 | 并 | 差")
    A = {1, 2, 3}
    B = {2, 3, 4}
    print("A =", A, " B =", B)
    S = {1}
    S.add(2)
    print("从 {1} 出发 add(2) ->", S)
    S.remove(2)
    print("remove(2) 后 ->", S)
    try:
        S.remove(99)
    except KeyError:
        print("remove(不存在的元素) -> KeyError")
    S.discard(99)
    print("discard(99)（不存在也不报错）->", S)
    print("A & B =", A & B)
    print("A | B =", A | B)
    print("A - B =", A - B)


if __name__ == "__main__":
    main()
