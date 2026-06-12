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

    section("iloc[:idx] 历史行情（13_ETF轮动_v3 · 1_1）")
    ohlc = pd.DataFrame(
        {
            "open": [1.0, 1.1, 1.2, 1.3, 1.4, 1.5],
            "high": [1.1, 1.2, 1.3, 1.4, 1.5, 1.6],
            "low": [0.9, 1.0, 1.1, 1.2, 1.3, 1.4],
            "close": [1.05, 1.15, 1.25, 1.35, 1.45, 1.55],
        }
    )
    df_all_v3 = {"510880.SH": ohlc}
    idx = 5
    history = df_all_v3["510880.SH"].iloc[:idx]
    close_series = history["close"]
    print("len(history) ->", len(history))
    print("history.index.tolist() ->", history.index.tolist())
    print("close_series.tolist() ->", close_series.tolist())

    section("布尔筛选定位交易日（13_ETF轮动_v3 · generate）")
    trade_days = pd.DataFrame(
        {
            "cal_date": ["20231227", "20231228", "20240102"],
            "pretrade_date": ["20231226", "20231227", "20231228"],
        }
    )
    trading_date = "20240102"
    current_row = trade_days.loc[trade_days["cal_date"] == trading_date]
    yesterday = current_row["pretrade_date"].iloc[0]
    print("current_row.to_dict(orient='records') ->", current_row.to_dict(orient="records"))
    print("yesterday ->", yesterday)

    section("loc 按日回填台账（1_2_ETF轮动_回测 · g.df）")
    portfolio_df = pd.DataFrame(
        index=trade_days["cal_date"],
        columns=["hold1", "cash", "value"],
    )
    dt_str = "20240102"
    portfolio_df.loc[dt_str, "cash"] = 100000.0
    portfolio_df.loc[dt_str, "hold1"] = "513100.SH"
    print("portfolio_df.loc[dt_str].to_dict() ->", portfolio_df.loc[dt_str].to_dict())

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
