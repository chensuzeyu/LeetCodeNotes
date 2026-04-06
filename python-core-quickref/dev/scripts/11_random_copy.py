"""对应 11-random-copy.md：random、copy；顺带演示 secrets 一句话"""

from __future__ import annotations

import copy
import random
import secrets

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("random：seed、randint、choice、shuffle、sample")
    random.seed(42)
    print("seed(42) 后 random() 两次:", round(random.random(), 6), round(random.random(), 6))
    print("randint(1, 6) 三次:", [random.randint(1, 6) for _ in range(3)])
    print("choice(['a', 'b', 'c']):", random.choice(["a", "b", "c"]))
    xs = [1, 2, 3, 4, 5]
    random.shuffle(xs)
    print("shuffle 后:", xs)
    print("sample(不重复):", random.sample(range(10), k=4))

    section("copy：浅拷贝 vs 深拷贝")
    nested = {"outer": {"x": [1, 2]}}
    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)
    nested["outer"]["x"].append(99)
    print("改 nested 内层列表后 shallow[\"outer\"][\"x\"] =", shallow["outer"]["x"])
    print("深拷贝不受影响 deep[\"outer\"][\"x\"] =", deep["outer"]["x"])

    section("secrets（安全随机，非 random）")
    print("token_hex(8) =", secrets.token_hex(8))


if __name__ == "__main__":
    main()
