"""对应 04-pandas-datetime-ffill-shape.md：to_datetime、DatetimeIndex、strftime、ffill。"""

from __future__ import annotations

import numpy as np
import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    raw = pd.DataFrame(
        {
            "trade_date": ["20240108", "20240109", "20240110"],
            "open": [10.0, 10.2, 10.3],
            "close": [10.1, np.nan, 10.4],
        }
    ).set_index("trade_date")

    section("to_datetime / DatetimeIndex")
    dt_df = raw.copy()
    dt_df.index = pd.to_datetime(dt_df.index, format="%Y%m%d")
    print("index class ->", type(dt_df.index).__name__)
    print("DatetimeIndex ->", dt_df.index.strftime("%Y-%m-%d").tolist())
    print("shape ->", dt_df.shape)

    section("ffill：补齐缺失行情")
    filled = dt_df[["open", "close"]].ffill()
    print("原始 close ->", dt_df["close"].tolist())
    print("ffill 后 close ->", filled["close"].tolist())

    section("strftime：改回 YYYYMMDD 字符串索引")
    yyyymmdd_df = filled.copy()
    yyyymmdd_df.index = yyyymmdd_df.index.strftime("%Y%m%d")
    print("string index ->", yyyymmdd_df.index.tolist())
    print("to_dict(orient='index') ->", yyyymmdd_df.to_dict(orient="index"))


if __name__ == "__main__":
    main()
