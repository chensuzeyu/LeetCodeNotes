"""对应 09-hkcodex-dates-marketdata.md：get_trade_days、fund_daily、index_daily。"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def load_hkcodex():
    script_path = Path(__file__).resolve()
    workspace = script_path.parents[4]
    helper = workspace / "Quant" / "HKCodex" / "HKCodex-CodeSets_v3" / "ensure_hkcodex_path.py"
    os.environ["HKCODEX_HOME"] = str(helper.parent)
    os.environ["HOME"] = str(helper.parent)
    os.environ["USERPROFILE"] = str(helper.parent)
    spec = importlib.util.spec_from_file_location("_hkcodex_path_bootstrap", helper)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载: {helper}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.ensure_hkcodex_path(script_path)
    import hkcodex as hx

    return helper, hx


def main() -> None:
    utf8_stdout()
    helper, hx = load_hkcodex()

    section("bootstrap：先挂上 hkcodex 路径")
    print("helper ->", helper)

    section("get_trade_days：交易日列表")
    trade_day = hx.get_trade_days(since="20240102", until="20240110")
    print("columns ->", trade_day.columns.tolist())
    print("cal_date ->", trade_day["cal_date"].tolist())

    section("fund_daily：ETF 日线")
    fund = hx.fund_daily(etf="510180.SH", start_date="20240102", end_date="20240110", adjust="front")
    print("fund shape ->", fund.shape)
    print("fund columns ->", fund.columns.tolist()[:8])
    print("fund index sample ->", list(map(str, fund.index[:3].tolist())))
    if not fund.empty and "close" in fund.columns:
        print("fund close head ->", fund["close"].head(3).round(4).tolist())
    else:
        print("fund is empty ->", True)

    section("index_daily：指数日线")
    index_df = hx.index_daily(index_code="000300.SH", start_date="20240102", end_date="20240110")
    print("index type ->", type(index_df).__name__)
    print("index name ->", index_df.name)
    print("index sample ->", [idx.strftime("%Y-%m-%d") for idx in index_df.index[:3]])
    print("pct_chg head ->", [round(float(v), 6) for v in index_df.head(3).tolist()])


if __name__ == "__main__":
    main()
