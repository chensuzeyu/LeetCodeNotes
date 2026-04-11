"""对应 10-1etf-chain.md：1_ETF轮动 的 txt 链路、portfolio.csv 与 cwd。"""

from __future__ import annotations

import io
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

    workspace = Path(__file__).resolve().parents[4]
    select_script = workspace / "Quant" / "HKCodex" / "HKCodex-CodeSets_v3" / "1_ETF轮动" / "1_1_ETF轮动_选.py"
    backtest_script = workspace / "Quant" / "HKCodex" / "HKCodex-CodeSets_v3" / "1_ETF轮动" / "1_2_ETF轮动_回测.py"

    section("真实脚本入口")
    print("select_script ->", select_script.name)
    print("backtest_script ->", backtest_script.name)

    section("模拟选股脚本：按交易日写 txt")
    selected = {
        "20240108": ["159915.SZ"],
        "20240109": ["510180.SH"],
    }
    base = Path(__file__).resolve().parent / "_tmp_1etf_chain_demo"
    out_dir = base / "ETF轮动"
    txt_payloads = {}
    for day, stocks in selected.items():
        txt_payloads[day] = "".join(f"{stock}\n" for stock in stocks)
    print("demo cwd ->", base)
    print("相对路径 'ETF轮动/20240108.txt' 落到 ->", out_dir / "20240108.txt")
    print("txt files ->", [f"{day}.txt" for day in selected])

    section("模拟回测脚本：按同一批日期读 txt")
    loaded = {}
    for day in selected:
        loaded[day] = txt_payloads[day].splitlines()
    print("loaded selections ->", loaded)
    print("日期完全对齐 ->", list(loaded.keys()) == list(selected.keys()))

    section("生成 portfolio.csv")
    portfolio = pd.DataFrame(
        {
            "hold1": [loaded["20240108"][0], loaded["20240109"][0]],
            "cash": [100000.0, 99800.0],
            "value": [100000.0, 100350.0],
        },
        index=["20240108", "20240109"],
    )
    portfolio_path = base / "ETF轮动_portfolio.csv"
    csv_buffer = io.StringIO()
    portfolio.to_csv(csv_buffer)
    print("portfolio columns ->", portfolio.columns.tolist())
    print("portfolio index ->", portfolio.index.tolist())
    print("portfolio logical path ->", portfolio_path)


if __name__ == "__main__":
    main()
