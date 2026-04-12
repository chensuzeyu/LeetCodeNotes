"""对应 10-dataclasses-typing.md：dataclass、typing 常用片段"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Protocol

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


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class HasArea(Protocol):
    def area(self) -> float: ...


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side


def total_area(shape: HasArea) -> float:
    return shape.area()


def main() -> None:
    utf8_stdout()
    section("dataclass：default_factory、实例")
    u = User("Ann", tags=["dev", "py"], score=97.5)
    print(u)
    v = User("Bob")
    v.tags.append("new")
    print(v)
    w = User("Cara")
    print("v.tags is w.tags ->", v.tags is w.tags)
    p = Point(3, 4)
    print("frozen Point:", p)
    print("Protocol total_area(Square(2)):", total_area(Square(2)))

    section("typing：Callable 粗略标注")
    twice: Callable[[int], int] = lambda x: x * 2
    maybe_score: Optional[float] = None
    print("Optional score ->", maybe_score)
    print("twice(21) =", twice(21))


if __name__ == "__main__":
    main()
