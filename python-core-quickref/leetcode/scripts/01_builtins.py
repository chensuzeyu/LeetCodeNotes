"""对应 01-builtins.md：len、range、enumerate、zip、sorted、min/max、sum、any/all、open"""

from __future__ import annotations

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
    pairs_lex = [(1, 8), (1, 9), (5, 2), (3, 7)]
    pairs_tie = [(1, 9), (1, 8), (5, 2), (3, 7)]
    print("pairs =", pairs)
    print("pairs_lex =", pairs_lex)
    print("min(pairs) =", min(pairs))
    print("min(pairs_lex) =", min(pairs_lex))
    print("min(pairs_lex, key=lambda p: p[0]) =", min(pairs_lex, key=lambda p: p[0]))
    print("pairs_tie =", pairs_tie)
    print("min(pairs_tie) =", min(pairs_tie))
    print("min(pairs_tie, key=lambda p: p[0]) =", min(pairs_tie, key=lambda p: p[0]))
    print("min(pairs, key=lambda p: p[1]) =", min(pairs, key=lambda p: p[1]))
    print("min(5, 2, 8) =", min(5, 2, 8))
    print("min([5, 2, 8]) =", min([5, 2, 8]))

    section("sum(iterable, start=0)")
    print("sum([1, 2, 3]) =", sum([1, 2, 3]))
    print("sum([], start=10) =", sum([], start=10))

    section("any / all（短路求值）")
    print("any([False, False, True]) =", any([False, False, True]))
    print("any([False, False]) =", any([False, False]))
    print("all([1, 2, 3]) =", all([1, 2, 3]))
    print("all([1, 2, 0]) =", all([1, 2, 0]))

    section('open(path, mode, encoding="utf-8")')
    # __file__ 是当前脚本自己的路径；resolve() 把它变成绝对路径。
    script_path = Path(__file__).resolve()
    print("script_path =", script_path)
    # parents[2] 表示向上退两级：scripts -> leetcode -> python-core-quickref。
    project_root = script_path.parents[2]
    print("project_root =", project_root)
    # 用 / 拼路径；Path 会按当前系统自动处理分隔符。
    sample_dir = project_root / ".tmp" / "leetcode"
    print("sample_dir =", sample_dir)
    # mkdir() 用来创建目录；
    # parents=True 表示上级目录不存在时也一起创建；
    # exist_ok=True 表示目录已存在时不报错。
    mkdir_result = sample_dir.mkdir(parents=True, exist_ok=True)
    print("sample_dir.mkdir(parents=True, exist_ok=True) ->", mkdir_result)
    print("sample_dir.exists() =", sample_dir.exists())
    sample_file = sample_dir / "sample.txt"
    print("sample_file =", sample_file)
    # mode="w" 表示写入：不存在就新建，已存在就覆盖；
    # encoding="utf-8" 表示按 UTF-8 规则保存文本，尽量避免乱码。
    # newline="\n" 表示按 \n 写入换行，让不同系统下的结果更一致。
    with open(sample_file, "w", encoding="utf-8", newline="\n") as f:
        f.write("hello\nworld\n")
    print("写入(mode=w, encoding=utf-8):", sample_file)
    print("sample_file.exists() =", sample_file.exists())
    # with 结束后文件会自动关闭；这里再打开一遍确认刚才写入的内容。
    with open(sample_file, encoding="utf-8") as f:
        lines = f.readlines()
    print("readlines() ->", lines)

    section("说明：更长序列 zip 补齐见 04（itertools.zip_longest）")


if __name__ == "__main__":
    main()
