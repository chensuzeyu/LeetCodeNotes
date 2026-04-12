"""对应 06-defaultdict-functools.md：defaultdict、functools"""

from __future__ import annotations

from collections import defaultdict
from functools import cache, lru_cache, reduce
from operator import add

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("defaultdict(list)：分组 / 邻接表")
    edges = [("a", 1), ("b", 2), ("a", 3)]
    g: defaultdict[str, list[int]] = defaultdict(list)
    for k, v in edges:
        g[k].append(v)
    print("edges ->", dict(g))

    section("defaultdict(int)：计数（与 Counter 对比）")
    dd: defaultdict[str, int] = defaultdict(int)
    for ch in "abacb":
        dd[ch] += 1
    print("频数 ->", dict(dd))

    section("defaultdict(set)")
    ds: defaultdict[str, set[int]] = defaultdict(set)
    ds["k"].add(1)
    ds["k"].add(1)
    print(dict(ds))

    section("functools.cache：递归（可哈希参数）")

    @cache
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print("fib(6) =", fib(6))
    print("cache_info =", fib.cache_info())

    section("lru_cache(maxsize=…)")
    calls = 0

    @lru_cache(maxsize=32)
    def path_count(m: int, n: int) -> int:
        nonlocal calls
        calls += 1
        if m == 0 or n == 0:
            return 1
        return path_count(m - 1, n) + path_count(m, n - 1)

    calls = 0
    print("path_count(3,3) =", path_count(3, 3), " 递归函数实际调用次数:", calls)
    print("lru_cache_info =", path_count.cache_info())

    section("lru_cache(maxsize=None)：接口与 cache 类似")
    calls_none = 0

    @lru_cache(maxsize=None)
    def path_count_unbounded(m: int, n: int) -> int:
        nonlocal calls_none
        calls_none += 1
        if m == 0 or n == 0:
            return 1
        return path_count_unbounded(m - 1, n) + path_count_unbounded(m, n - 1)

    calls_none = 0
    print("path_count_unbounded(3,3) =", path_count_unbounded(3, 3), " 递归函数实际调用次数:", calls_none)
    print("lru_cache_none_info =", path_count_unbounded.cache_info())

    section("reduce（偶尔一把梭）")
    print("reduce(add, [1,2,3,4]) =", reduce(add, [1, 2, 3, 4]))
    print("reduce(add, [1,2,3,4], 0) =", reduce(add, [1, 2, 3, 4], 0))
    print("reduce(add, [], 0) =", reduce(add, [], 0))


if __name__ == "__main__":
    main()
