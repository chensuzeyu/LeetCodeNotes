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
    learn_src = workspace / "Quant" / "HKCodex-learn" / "src"
    os.environ["HKCODEX_HOME"] = str(helper.parent)
    os.environ["HOME"] = str(helper.parent)
    os.environ["USERPROFILE"] = str(helper.parent)
    if learn_src.is_dir() and not os.environ.get("HKCODEX_LEARN_SRC"):
        os.environ["HKCODEX_LEARN_SRC"] = str(learn_src)
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

    section("get_trade_days：区间查询（v3 第 110 行）")
    trade_day = hx.get_trade_days(since="20240102", until="20240106")
    print(trade_day.head(3).to_string())
    print("dtypes ->", trade_day.dtypes.to_dict())

    section("get_trade_days：count 往前取 warmup（v3 第 112 行示意）")
    warmup_sample = hx.get_trade_days(until="20240110", count=5)
    print(warmup_sample.to_string())
    print("最早 cal_date ->", warmup_sample.iloc[0]["cal_date"])

    section("fund_daily：510880.SH 前复权（v3 第 118 行）")
    fund = hx.fund_daily(etf="510880.SH", start_date="20240102", end_date="20240106", adjust="front")
    print("shape ->", fund.shape)
    print("index.name ->", fund.index.name, "| index.dtype ->", fund.index.dtype)
    print("columns ->", fund.columns.tolist())
    print()
    print(fund.head(3).to_string())
    ohlc = fund[["open", "high", "low", "close"]].reset_index(drop=True)
    print()
    print("v3 切片 ohlc.head(3):")
    print(ohlc.head(3).to_string())

    section("index_daily：沪深300 日涨跌幅")
    index_s = hx.index_daily(index_code="000300.SH", start_date="20240102", end_date="20240106")
    print("type ->", type(index_s).__name__, "| name ->", index_s.name)
    print(index_s.head(3).to_string())


if __name__ == "__main__":
    main()
