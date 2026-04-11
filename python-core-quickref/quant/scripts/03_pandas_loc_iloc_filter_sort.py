"""对应 03-pandas-loc-iloc-filter-sort.md：loc、iloc、筛选、排序、去重。"""

from __future__ import annotations

import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    df = pd.DataFrame(
        {
            "trade_date": ["20240108", "20240109", "20240109", "20240110"],
            "etf": ["510180.SH", "159915.SZ", "513100.SH", "159915.SZ"],
            "score": [0.91, 1.08, 1.02, 0.88],
        }
    ).set_index("trade_date")

    section("loc / iloc")
    print("df.loc['20240109'].to_dict(orient='records') ->", df.loc["20240109"].to_dict(orient="records"))
    print("df.iloc[1].to_dict() ->", df.iloc[1].to_dict())

    section("布尔筛选 / 列子集")
    picked = df.loc[df["score"] > 1.0, ["etf", "score"]]
    print("df[df['score'] > 1.0][['etf', 'score']] ->", picked.to_dict(orient="records"))

    section("sort_values / drop_duplicates")
    sorted_df = df.sort_values("score", ascending=False)
    dedup = sorted_df.drop_duplicates(subset=["etf"], keep="first")
    print("sort_values('score', ascending=False) ->", sorted_df.reset_index().to_dict(orient="records"))
    print("drop_duplicates(subset=['etf']) ->", dedup.reset_index().to_dict(orient="records"))


if __name__ == "__main__":
    main()
