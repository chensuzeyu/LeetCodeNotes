"""对应 10-dataclasses-typing.md：dataclass、typing 常用片段"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
    score: Optional[float] = None


def main() -> None:
    utf8_stdout()
    section("dataclass：default_factory、实例")
    u = User("Ann", tags=["dev", "py"], score=97.5)
    print(u)
    v = User("Bob")
    v.tags.append("new")
    print(v)

    section("typing：Callable 粗略标注")
    twice: Callable[[int], int] = lambda x: x * 2
    print("twice(21) =", twice(21))


if __name__ == "__main__":
    main()
