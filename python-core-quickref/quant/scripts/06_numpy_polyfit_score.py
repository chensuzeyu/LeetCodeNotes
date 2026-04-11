"""对应 06-numpy-polyfit-score.md：polyfit、拟合值、r_squared、ETF 动量打分。"""

from __future__ import annotations

import math

import numpy as np

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    close = np.array([100.0, 101.0, 103.0, 106.0, 108.0])
    y = np.log(close)
    x = np.arange(y.size)
    slope, intercept = np.polyfit(x, y, 1)
    fitted = slope * x + intercept
    annualized_returns = math.pow(math.exp(slope), 250) - 1
    r_squared = 1 - (np.sum((y - fitted) ** 2) / ((len(y) - 1) * np.var(y, ddof=1)))
    score = annualized_returns * r_squared

    section("np.polyfit：斜率与截距")
    print("close ->", close.tolist())
    print("x ->", x.tolist())
    print("log(close) ->", [round(v, 6) for v in y.tolist()])
    print("slope =", round(float(slope), 6), " intercept =", round(float(intercept), 6))

    section("拟合值 / r_squared")
    print("fitted ->", [round(v, 6) for v in fitted.tolist()])
    print("r_squared ->", round(float(r_squared), 6))

    section("按 1_ETF轮动 风格计算得分")
    print("annualized_returns ->", round(float(annualized_returns), 6))
    print("score ->", round(float(score), 6))


if __name__ == "__main__":
    main()
