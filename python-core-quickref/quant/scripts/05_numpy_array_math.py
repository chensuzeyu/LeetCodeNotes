"""对应 05-numpy-array-math.md：array、arange、广播、log、exp、mean、var、where。"""

from __future__ import annotations

import numpy as np

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    section("array / arange / 广播")
    a = np.array([1.0, 2.0, 3.0])
    b = np.arange(3)
    print("a ->", a.tolist())
    print("np.arange(3) ->", b.tolist())
    print("a + 10 ->", (a + 10).tolist())
    print("a * np.array([1, 10, 100]) ->", (a * np.array([1, 10, 100])).tolist())

    section("log / exp / where")
    x = np.array([1.0, np.e, np.e ** 2])
    logged = np.log(x)
    print("np.log([1, e, e^2]) ->", [round(v, 6) for v in logged.tolist()])
    print("np.exp([0, 1, 2]) ->", [round(v, 6) for v in np.exp(np.array([0.0, 1.0, 2.0])).tolist()])
    print("np.where(a > 1.5, 'high', 'low') ->", np.where(a > 1.5, "high", "low").tolist())

    section("mean / var")
    scores = np.array([0.9, 1.1, 1.0, 1.2])
    print("scores ->", scores.tolist())
    print("np.mean(scores) ->", round(float(np.mean(scores)), 6))
    print("np.var(scores, ddof=1) ->", round(float(np.var(scores, ddof=1)), 6))


if __name__ == "__main__":
    main()
