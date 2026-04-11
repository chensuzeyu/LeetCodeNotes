"""对应 02-pandas-readwrite-index.md：read_csv、to_csv、index_col、set_index、reset_index。"""

from __future__ import annotations

import io
import os
import tempfile
from pathlib import Path

import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    csv_text = "trade_date,etf,score\n20240108,510180.SH,0.91\n20240109,159915.SZ,1.08\n"

    section("read_csv：默认整数索引 / index_col")
    df_plain = pd.read_csv(io.StringIO(csv_text))
    df_idx = pd.read_csv(io.StringIO(csv_text), index_col="trade_date")
    print("read_csv ->", df_plain.to_dict(orient="records"))
    print("read_csv(index_col='trade_date') index ->", df_idx.index.astype(str).tolist())
    print("index_col 后首行 ->", df_idx.iloc[0].to_dict())

    section("set_index / reset_index")
    df_set = df_plain.set_index("trade_date")
    print("set_index('trade_date') columns ->", df_set.columns.tolist())
    print("set_index 后索引 ->", df_set.index.astype(str).tolist())
    print("reset_index() ->", df_set.reset_index().to_dict(orient="records"))

    section("to_csv：写盘后再读回")
    fd, temp_name = tempfile.mkstemp(prefix="quant_scores_", suffix=".csv")
    os.close(fd)
    out = Path(temp_name)
    try:
        df_set.to_csv(out)
        read_back = pd.read_csv(out, index_col="trade_date")
        print("写入 ->", out)
        print("read back ->", read_back.to_dict(orient="index"))
    finally:
        if out.exists():
            out.unlink()


if __name__ == "__main__":
    main()
