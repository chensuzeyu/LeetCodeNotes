"""对应 04-collections-itertools.md：Counter、deque、itertools"""

from __future__ import annotations

import itertools
import operator
from collections import Counter, deque

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("Counter：频次、most_common、update")
    c = Counter(["a", "b", "a", "a", "c"])
    print("Counter([...]) ->", c)
    print("c['a'] =", c["a"], "  c['z']（未见过的键）=", c["z"])
    print("c.most_common(2) =", c.most_common(2))
    c.update(["a", "b", "b"])
    print("update(['a','b','b']) 后 ->", dict(c))

    section("deque：appendleft / popleft；可选 maxlen（滑动窗口）")
    dq: deque[int] = deque([1, 2])
    dq.appendleft(0)
    dq.append(3)
    print("deque 操作后 list(dq) =", list(dq))
    print("popleft ->", dq.popleft(), " pop ->", dq.pop(), " 剩下", list(dq))
    win: deque[int] = deque([1, 2, 3], maxlen=3)
    win.append(4)
    print("deque([1,2,3], maxlen=3).append(4) ->", list(win), "（左端被挤掉）")

    section("itertools：permutations / combinations")
    print("permutations([1,2,3], 2) =", list(itertools.permutations([1, 2, 3], 2)))
    print("combinations([1,2,3], 2) =", list(itertools.combinations([1, 2, 3], 2)))

    section("accumulate：默认求和（前缀和）；func= 可改累乘等")
    print("accumulate([1,2,3,4]) ->", list(itertools.accumulate([1, 2, 3, 4])))
    print(
        "accumulate([1,2,3,4], func=operator.mul) ->",
        list(itertools.accumulate([1, 2, 3, 4], func=operator.mul)),
    )

    section("groupby：相邻相同键分组；无序数据需先 sorted(..., key=)")
    runs = "aaabbbcca"
    groups = [(k, list(g)) for k, g in itertools.groupby(runs)]
    print("runs =", repr(runs), "-> groupby ->", groups)
    raw = [(2, "a"), (1, "b"), (2, "c")]
    keyfn = lambda t: t[0]
    ordered = sorted(raw, key=keyfn)
    print("raw =", raw, " sorted(key=首元) ->", ordered)
    g2 = [(k, list(g)) for k, g in itertools.groupby(ordered, key=keyfn)]
    print("groupby(sorted, key=首元) ->", g2)

    section("zip_longest：与内置 zip 对比（补齐）")
    print("zip([1,2], [10]) ->", list(zip([1, 2], [10])))
    print(
        "zip_longest([1,2], [10], fillvalue=0) ->",
        list(itertools.zip_longest([1, 2], [10], fillvalue=0)),
    )


if __name__ == "__main__":
    main()
