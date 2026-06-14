"""对应 01-pandas-series-dataframe.md：Series、DataFrame、列与索引（含 13_ETF轮动_v3）。"""

from __future__ import annotations

import numpy as np
import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def zscore(series: pd.Series) -> pd.Series:
    std = series.std(ddof=0)
    if std == 0 or np.isnan(std):
        return pd.Series(0, index=series.index)
    return (series - series.mean()) / std


def main() -> None:
    utf8_stdout()

    section("Series：值、索引、name")
    s = pd.Series([0.91, 1.08, 0.97], index=["510180.SH", "159915.SZ", "513100.SH"], name="score")
    print("Series.to_dict() ->", s.to_dict())
    print("Series.tolist() ->", s.tolist())
    print("Series.index ->", s.index.tolist())
    print("Series.name ->", s.name)

    section("Series 构造对照：dict / list / list+index")
    from_dict = pd.Series({"bias": 0.2, "slope": 0.3, "efficiency": 0.5}, dtype="float64")
    from_list = pd.Series([0.2, 0.3, 0.5])
    print("dict 构造 index ->", from_dict.index.tolist())
    print("dict 构造:\n", from_dict.to_string())
    print("list 默认 index ->", from_list.index.tolist())
    print("list 默认:\n", from_list.to_string())

    section("dict 权重 + 归一化（13_ETF轮动_v3 · weights）")
    factor_weights = {"bias": 0.2, "slope": 0.3, "efficiency": 0.5}
    weights = pd.Series(factor_weights, dtype="float64")
    weights = weights / weights.sum()
    print("weights:\n", weights.to_string())
    print("type(weights) ->", type(weights).__name__)
    print("weights.sum() ->", weights.sum())

    section("标量广播 Series（zscore 退化分支）")
    flat = pd.Series({"510880.SH": 1.0, "159915.SZ": 1.0, "513100.SH": 1.0})
    zeros = pd.Series(0, index=flat.index)
    print("pd.Series(0, index=...) ->", zeros.to_dict())

    section("空 Series 填分 + idxmax（1_ETF轮动）")
    etf_libs = ["510180.SH", "159915.SZ", "513100.SH", "518880.SH"]
    scores = pd.Series(index=etf_libs, dtype="float64")
    for stk, val in zip(etf_libs, [12.3, 8.1, 45.6, 3.2]):
        scores[stk] = val
    print("scores:\n", scores.to_string())
    print("scores.idxmax() ->", scores.idxmax())

    section("DataFrame：从 dict/list 构造")
    df = pd.DataFrame(
        {
            "etf": ["510180.SH", "159915.SZ"],
            "score": [0.91, 1.08],
            "hold": [False, True],
        },
        index=["20240108", "20240109"],
    )
    print("DataFrame.to_dict(orient='index') ->", df.to_dict(orient="index"))
    print("DataFrame.to_dict(orient='records') ->", df.to_dict(orient="records"))
    print("columns ->", df.columns.tolist())
    print("index ->", df.index.tolist())

    section("axis 与 dim 0/1（factor_df 必读）")
    etf_libs_axis = ["510880.SH", "159915.SZ", "513100.SH", "518880.SH"]
    bias_col = pd.Series([12.3, 8.1, 45.6, 3.2], index=etf_libs_axis)
    z_bias = zscore(bias_col)
    print("bias 列原始值 ->", bias_col.tolist())
    print("zscore(bias) 列:\n", z_bias.to_string())
    mini = pd.DataFrame(
        {"bias": [12.3, 8.1, 45.6, 3.2]},
        index=etf_libs_axis,
    )
    arr = mini.values
    print("mini.shape ->", mini.shape, "  # (行, 列) = dim0, dim1")
    print("np.mean(arr, axis=0) ->", np.mean(arr, axis=0).tolist(), "  # 沿行聚合，每列一个数")
    # 固定 vs 全选：arr[:, j] 固定列、沿行切；arr[i, :] 固定行、沿列切
    grid = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])
    print("arr[:, 1] 固定列1、沿dim0 ->", grid[:, 1].tolist(), "  # 竖条，长度4")
    print("arr[0, :] 固定行0、沿dim1 ->", grid[0, :].tolist(), "  # 横条，长度3")

    section("空 DataFrame 预建因子表 + at + apply（13_ETF轮动_v3 · factor_df）")
    etf_libs_v3 = ["510880.SH", "159915.SZ", "513100.SH", "518880.SH"]
    factor_df = pd.DataFrame(index=etf_libs_v3, columns=["bias", "slope", "efficiency"], dtype="float64")
    raw_scores = {
        "510880.SH": (12.3, 1.2, 0.5),
        "159915.SZ": (8.1, 0.8, 0.3),
        "513100.SH": (45.6, 2.1, 1.1),
        "518880.SH": (3.2, 0.5, 0.2),
    }
    for stk, (b, sl, ef) in raw_scores.items():
        factor_df.at[stk, "bias"] = b
        factor_df.at[stk, "slope"] = sl
        factor_df.at[stk, "efficiency"] = ef
    print("factor_df:\n", factor_df.to_string())
    z_factors = factor_df.apply(zscore, axis=0)
    print("z_factors.apply(zscore, axis=0) columns ->", z_factors.columns.tolist())
    print("z_factors index ->", z_factors.index.tolist())

    section("行情列裁剪 + reset_index(drop=True)（13_ETF轮动_v3 · df_all）")
    bars = pd.DataFrame(
        {
            "open": [1.0, 1.1, 1.2],
            "high": [1.1, 1.2, 1.3],
            "low": [0.9, 1.0, 1.1],
            "close": [1.05, 1.15, 1.25],
            "vol": [100, 110, 120],
        },
        index=["20240102", "20240103", "20240105"],
    )
    trimmed = bars[["open", "high", "low", "close"]].reset_index(drop=True)
    print("trimmed.columns ->", trimmed.columns.tolist())
    print("trimmed.index ->", trimmed.index.tolist())
    print("trimmed.shape ->", trimmed.shape)

    section("取列当 Series + iloc 取单元格（13_ETF轮动_v3 · 日历）")
    trade_days = pd.DataFrame(
        {
            "cal_date": ["20231227", "20231228", "20240102"],
            "pretrade_date": ["20231226", "20231227", "20231228"],
        }
    )
    start_date = trade_days.iloc[0]["cal_date"]
    cal_dates = trade_days["cal_date"].tolist()
    print("start_date ->", start_date)
    print("trade_days['cal_date'].tolist() ->", cal_dates)
    print("type(trade_days['cal_date']) ->", type(trade_days["cal_date"]).__name__)

    section("Z-Score 加权融合 → combined_scores（13_ETF轮动_v3）")
    combined_scores = z_factors.mul(weights, axis=1).sum(axis=1)
    combined_scores = combined_scores.sort_values(ascending=False)
    top_candidate = combined_scores.index[0]
    top_score = combined_scores.iloc[0]
    current_hold = "159915.SZ"
    current_score = combined_scores.get(current_hold, np.nan)
    print("combined_scores:\n", combined_scores.to_string())
    print("top_candidate ->", top_candidate)
    print("top_score ->", top_score)
    print("combined_scores.get(current_hold, nan) ->", current_score)
    with_nan = combined_scores.copy()
    with_nan.iloc[1] = np.nan
    dropped = with_nan.dropna().sort_values(ascending=False)
    print("dropna 后 index ->", dropped.index.tolist())

    section("回测台账空表 + loc 赋值（1_2_ETF轮动_回测 · g.df）")
    col_names = ["hold1", "vol1", "close1", "cash", "value", "value_cal"]
    portfolio_df = pd.DataFrame(index=trade_days["cal_date"], columns=col_names)
    portfolio_df.loc["20240102", "cash"] = 100000.0
    portfolio_df.loc["20240102", "hold1"] = "513100.SH"
    print("portfolio_df.loc['20240102'].to_dict() ->", portfolio_df.loc["20240102"].to_dict())

    section("dict 分析结果 → Series（1_2 · pnl）")
    pnl = pd.Series({"20240102": 0.001, "20240103": -0.002, "20240105": 0.0005})
    print("pnl:\n", pnl.to_string())
    print("pnl.index ->", pnl.index.tolist())

    section("列访问 / head")
    print("df['score'].tolist() ->", df["score"].tolist())
    print("type(df['score']) ->", type(df["score"]).__name__)
    print("type(df[['etf', 'score']]) ->", type(df[["etf", "score"]]).__name__)
    print("df[['etf', 'score']].to_dict(orient='records') ->", df[["etf", "score"]].to_dict(orient="records"))
    print("df.head(1).to_dict(orient='index') ->", df.head(1).to_dict(orient="index"))


if __name__ == "__main__":
    main()
