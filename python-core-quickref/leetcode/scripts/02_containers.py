"""对应 02-containers.md：list / tuple / dict / str / set 常用方法"""

from __future__ import annotations

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    section("list：append / extend / pop / remove / insert / reverse / clear / 切片")
    nums = [1, 2]
    nums.append(3)
    print("append(3) ->", nums)
    nums_append = [1, 2]
    nums_append.append([4, 5])
    print("append([4, 5]) ->", nums_append)
    nums.extend([4, 5])
    print("extend([4, 5]) ->", nums)

    last = nums.pop()
    print("pop() ->", last, " nums ->", nums)
    mid = nums.pop(1)
    print("pop(1) ->", mid, " nums ->", nums)
    try:
        nums.pop(99)
    except IndexError as e:
        print("pop(99) -> IndexError:", e)

    removed = [1, 4, 4, 2]
    print("初始 removed =", removed)
    removed.remove(4)
    print("remove(4) ->", removed)
    removed.remove(4)
    print("再次 remove(4) ->", removed)
    try:
        removed.remove(99)
    except ValueError as e:
        print("remove(99) -> ValueError:", e)
    try:
        removed.remove(1, 2)
    except TypeError as e:
        print("remove(1, 2) -> TypeError:", e)
    removed.insert(1, 8)
    print("insert(1, 8) ->", removed)

    rev = [9, 2, 3]
    reverse_result = rev.reverse()
    print("rev.reverse() 返回 ->", reverse_result, " rev ->", rev)
    cleared = [7, 8]
    cleared.clear()
    print("clear() 后 ->", cleared)
    sliced = [9, 2, 3, 4]
    print("nums[1:3]（左闭右开）->", sliced[1:3])
    print("nums[::2]（step=2）->", sliced[::2])
    print("nums[::-1]（新序列，原列表不变）->", sliced[::-1], " 原 nums =", sliced)

    section("list 与 tuple：可变 / 不可变")
    pairs_tuple = [(1, 9), (5, 2), (3, 7)]
    pairs_list = [[1, 9], [5, 2], [3, 7]]
    print("min([(1, 9), (5, 2), (3, 7)]) ->", min(pairs_tuple))
    print("min([[1, 9], [5, 2], [3, 7]]) ->", min(pairs_list))
    pairs_list[0][0] = 8
    print("列表可改：pairs_list[0][0] = 8 后 ->", pairs_list)
    t = (1, 9)
    try:
        t[0] = 8
    except TypeError as e:
        print("元组不可改：t[0] = 8 -> TypeError:", e)

    section(
        "dict：[] / get / setdefault / pop / popitem / update / keys / values / items / copy / clear"
    )
    d: dict[str, int] = {"a": 1}
    print("d =", d)
    print("d['a'] =", d["a"])
    try:
        _ = d["missing"]
    except KeyError as e:
        print("d['missing'] -> KeyError:", e)
    print("d.get('b', 0) =", d.get("b", 0), " d ->", d)
    print("setdefault('a', 99) ->", d.setdefault("a", 99), " d ->", d)
    print("setdefault('b', 2) ->", d.setdefault("b", 2), " d ->", d)
    print("'a' in d =", "a" in d, "  'z' in d =", "z" in d)
    print("pop('b') ->", d.pop("b"), " d ->", d)
    print("pop('missing', -1) ->", d.pop("missing", -1), " d ->", d)
    d.update({"b": 2, "c": 3})
    print("update({'b': 2, 'c': 3}) 后 d ->", d)
    print("list(d.keys()) ->", list(d.keys()))
    print("list(d.values()) ->", list(d.values()))
    print("list(d.items()) ->", list(d.items()))
    print("copy() ->", d.copy())
    print("popitem() ->", d.popitem(), " d ->", d)
    for k, v in d.items():
        print(f"  item: {k!r} -> {v}")
    d.clear()
    print("clear() 后 ->", d)

    section("str：split / strip / join / 切片")
    s = "  a,b, c  \n"
    print("repr(s) =", repr(s))
    print("'hello   world\\nfoo'.split() ->", "hello   world\nfoo".split())
    print("'a,,b'.split(',') ->", "a,,b".split(","))
    print("s.split(',') ->", s.split(","))
    print("s.strip() ->", repr(s.strip()))
    print(repr("  a  b  \n") + ".strip() ->", repr("  a  b  \n".strip()))
    print(repr("  abc\n") + ".lstrip() ->", repr("  abc\n".lstrip()))
    print(repr("abc  \n") + ".rstrip() ->", repr("abc  \n".rstrip()))
    print("'--'.join(['x', 'y', 'z']) ->", "--".join(["x", "y", "z"]))
    try:
        "--".join(["x", 1])
    except TypeError as e:
        print("'--'.join(['x', 1]) -> TypeError:", e)
    print("'hello'[1:4]（左闭右开）->", "hello"[1:4])

    section("set：add / remove / discard / update / union / intersection / difference / copy / clear")
    A = {1, 2, 3}
    B = {2, 3, 4}
    print("A =", A, " B =", B)
    S = {1}
    S.add(2)
    print("add(2) 后 sorted(S) ->", sorted(S))
    S.remove(2)
    print("remove(2) 后 sorted(S) ->", sorted(S))
    try:
        S.remove(99)
    except KeyError:
        print("remove(不存在的元素) -> KeyError")
    S.discard(99)
    print("discard(99)（不存在也不报错）后 sorted(S) ->", sorted(S))
    print("sorted(A & B) ->", sorted(A & B))
    print("sorted(A | B) ->", sorted(A | B))
    print("sorted(A - B) ->", sorted(A - B))
    S2 = {1}
    S2.update({2, 3})
    print("update({2, 3}) 后 sorted(S2) ->", sorted(S2))
    print("sorted(A.union(B)) ->", sorted(A.union(B)), " 原 A 仍为", sorted(A))
    print(
        "sorted(A.intersection(B)) ->",
        sorted(A.intersection(B)),
        " 原 A 仍为",
        sorted(A),
    )
    print("sorted(A.difference(B)) ->", sorted(A.difference(B)), " 原 A 仍为", sorted(A))
    copy_s = A.copy()
    print("copy() ->", sorted(copy_s))
    copy_s.clear()
    print("clear() 后 sorted(copy_s) ->", sorted(copy_s))


if __name__ == "__main__":
    main()
