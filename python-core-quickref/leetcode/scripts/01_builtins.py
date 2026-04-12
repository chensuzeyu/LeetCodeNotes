"""对应 01-builtins.md：len、range、enumerate、zip、sorted、min/max、sum、any/all、open"""

from __future__ import annotations

import tempfile
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("len / range（终点不含；参数须为整数语义）")
    nums = [2, 7, 11, 15]
    print("nums =", nums)
    print("len(nums) =", len(nums))
    print("list(range(len(nums))) =", list(range(len(nums))))
    print("list(range(1, 4)) = range(a,b) ->", list(range(1, 4)))
    print("list(range(4, 1, -1)) = step=-1 ->", list(range(4, 1, -1)))

    section("enumerate(iterable, start=0)")
    items = ["a", "b", "c"]
    print("items =", items)
    for start in (0, 1, 2):
        print(f"  start={start}:")
        for i, x in enumerate(items, start=start):
            print(f"    i={i}, x={x!r}")  # !r：repr(x)，字符串带引号

    section("zip：并行遍历；长度以最短为准（尾部丢弃）")
    a = [1, 2, 3]
    b = [10, 20]
    print("a =", a, " b =", b)
    print("list(zip(a, b)) =", list(zip(a, b)))
    print("for i, j in zip(a, b):", end=" ")
    parts = [f"({i}+{j})" for i, j in zip(a, b)]
    print(" ".join(parts))

    section("sorted：返回新列表；key= / reverse=")
    arr = [3, 1, 4, 1, 5]
    print("原 arr =", arr)
    t = sorted(arr)
    print("sorted(arr) ->", t, " 原 arr 仍为", arr)
    arr.sort()
    print("arr.sort() 后 arr =", arr, "（list.sort 原地排序，返回 None）")

    words = ["bb", "a", "ccc"]
    print('sorted(words, key=len) ->', sorted(words, key=len))
    students = [
        {"name": "Tom", "age": 18},
        {"name": "Amy", "age": 16},
        {"name": "Bob", "age": 17},
    ]
    print(
        "sorted(students, key=lambda x: x['age']) ->",
        sorted(students, key=lambda x: x["age"]),
    )
    print("sorted(arr, reverse=True) ->", sorted(arr, reverse=True))

    section("min / max：可 key=；多标量用 min(a,b,c)；序列用 min(seq)")
    pairs = [(1, 9), (5, 2), (3, 7)]
    print("pairs =", pairs)
    print("min(pairs) =", min(pairs))
    print("min(pairs, key=lambda p: p[1]) =", min(pairs, key=lambda p: p[1]))
    print("min(5, 2, 8) =", min(5, 2, 8))
    print("min([5, 2, 8]) =", min([5, 2, 8]))

    section("sum(iterable, start=0)")
    print("sum([1, 2, 3]) =", sum([1, 2, 3]))
    print("sum([], start=10) =", sum([], start=10))

    section("any / all（短路求值）")
    print("any([False, False, True]) =", any([False, False, True]))
    print("all([1, 2, 0]) =", all([1, 2, 0]))

    section('open(path, mode, encoding="utf-8")')
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "sample.txt"
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("hello\nworld\n")
        print("写入(mode=w, encoding=utf-8):", p)
        with open(p, encoding="utf-8") as f:
            lines = f.readlines()
        print("readlines() ->", lines)

    section("说明：更长序列 zip 补齐见 04（itertools.zip_longest）")


if __name__ == "__main__":
    main()
