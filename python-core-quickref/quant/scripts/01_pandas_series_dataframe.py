"""对应 01-pandas-series-dataframe.md：Series、DataFrame、列与索引。"""

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

    section("Series：值、索引、name")
    s = pd.Series([0.91, 1.08, 0.97], index=["510180.SH", "159915.SZ", "513100.SH"], name="score")
    print("Series.to_dict() ->", s.to_dict())
    print("Series.index ->", s.index.tolist())
    print("Series.name ->", s.name)

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
    print("columns ->", df.columns.tolist())
    print("index ->", df.index.tolist())

    section("列访问 / head")
    print("df['score'].tolist() ->", df["score"].tolist())
    print("df[['etf', 'score']].to_dict(orient='records') ->", df[["etf", "score"]].to_dict(orient="records"))
    print("df.head(1).to_dict(orient='index') ->", df.head(1).to_dict(orient="index"))


if __name__ == "__main__":
    main()
