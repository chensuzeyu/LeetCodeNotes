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

    # index 可重复（同 dict 键唯一不同）；20240109 两行用于演示 df.loc 多行返回
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

    section("iloc 行切片 + 取列（1_ETF轮动）")
    bars = pd.DataFrame(
        {"close": [3.50, 3.52, 3.55, 3.53, 3.58, 3.60, 3.62, 3.65]},
        index=[
            "20240102",
            "20240103",
            "20240105",
            "20240108",
            "20240109",
            "20240110",
            "20240111",
            "20240112",
        ],
    )
    df_all = {"510180.SH": bars}
    stk, reg_num, idx = "510180.SH", 3, 5
    temp_close = df_all[stk].iloc[idx - reg_num : idx]["close"]
    print("temp_close.index ->", temp_close.index.tolist())
    print("temp_close.tolist() ->", temp_close.tolist())
    print("len(temp_close) ->", len(temp_close))
    print("type(temp_close) ->", type(temp_close).__name__)

    section("布尔筛选 / 列子集")
    picked = df.loc[df["score"] > 1.0, ["etf", "score"]]
    print("df[df['score'] > 1.0][['etf', 'score']] ->", picked.to_dict(orient="records"))

    section("sort_values / drop_duplicates")
    sorted_asc = df.sort_values("score")
    sorted_df = df.sort_values("score", ascending=False)
    dedup = sorted_df.drop_duplicates(subset=["etf"], keep="first")
    print("sort_values('score') ->", sorted_asc.reset_index().to_dict(orient="records"))
    print("sort_values('score', ascending=False) ->", sorted_df.reset_index().to_dict(orient="records"))
    print("drop_duplicates(subset=['etf']) ->", dedup.reset_index().to_dict(orient="records"))


if __name__ == "__main__":
    main()
