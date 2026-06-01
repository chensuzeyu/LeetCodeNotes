"""对应 11-etf-v3-hkcodex.md：ETF轮动_v3 用到的全部 hkcodex 接口。"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pandas as pd

from _io_util import utf8_stdout


ETF_LIBS = ["510880.SH", "159915.SZ", "513100.SH", "518880.SH"]
START = "20240102"
END = "20240110"
WARMUP = 25


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


def demo_bootstrap(helper) -> None:
    section("0 · bootstrap（1_1 / 1_2 / generate 头部相同）")
    print("helper ->", helper)
    print("HKCODEX_HOME ->", os.environ.get("HKCODEX_HOME"))
    print("脚本内模式: 向上查找 ensure_hkcodex_path.py -> ensure_hkcodex_path(__file__) -> import hkcodex as hx")


def demo_get_trade_days(hx) -> tuple[pd.DataFrame, pd.DataFrame]:
    section("1 · get_trade_days · 1_1 策略区间（第 110 行）")
    strategy_trade_days = hx.get_trade_days(since=START, until=END)
    print(strategy_trade_days.head(3).to_string())
    print("... 共", len(strategy_trade_days), "行")

    section("2 · get_trade_days · 1_1 warmup（第 112 行）")
    trade_days_with_warmup = hx.get_trade_days(
        until=END, count=len(strategy_trade_days) + WARMUP
    )
    print("warmup 后总行数 ->", len(trade_days_with_warmup))
    print("扩完 start_date ->", trade_days_with_warmup.iloc[0]["cal_date"])
    print(trade_days_with_warmup.head(3).to_string())

    section("3 · get_trade_days · generate 单日（第 139 行）")
    trading_date = "20240110"
    gen_days = hx.get_trade_days(until=trading_date, count=WARMUP + 60)
    row = gen_days.loc[gen_days["cal_date"] == trading_date].iloc[0]
    print("trading_date ->", trading_date)
    print("pretrade_date（行情截止日）->", row["pretrade_date"])
    print("gen 日历 tail(3):")
    print(gen_days.tail(3).to_string())

    section("4 · get_trade_days · 1_2 回测日历（第 154 行）")
    trade_day = hx.get_trade_days(since=START, until=END)
    print("回测 df.index 将用 cal_date ->", trade_day["cal_date"].head(3).tolist())
    return strategy_trade_days, trade_days_with_warmup


def demo_fund_daily(hx, trade_days_with_warmup: pd.DataFrame) -> None:
    start_date = trade_days_with_warmup.iloc[0]["cal_date"]
    stk = ETF_LIBS[0]

    section("5 · fund_daily · 1_1 选股（第 118 行）")
    raw = hx.fund_daily(etf=stk, start_date=start_date, end_date=END, adjust="front")
    ohlc_1_1 = raw[["open", "high", "low", "close"]].reset_index(drop=True)
    print(f"{stk} 原始 index.name ->", raw.index.name)
    print(raw.head(2).to_string())
    print()
    print("1_1 reset_index 后 iloc[:idx] 切片（idx=3 示意）:")
    print(ohlc_1_1.iloc[:3].to_string())

    section("6 · fund_daily · 1_2 回测喂 backtrader（第 179-181 行）")
    bt_df = raw.copy()
    bt_df.index = pd.to_datetime(bt_df.index, format="%Y%m%d")
    bt_df = bt_df[["open", "high", "low", "close"]].ffill()
    print("index 变为 DatetimeIndex:")
    print(bt_df.head(3).to_string())

    section("7 · fund_daily · generate 实盘（第 155 行）")
    trading_date = "20240110"
    gen_days = hx.get_trade_days(until=trading_date, count=WARMUP + 60)
    yesterday = gen_days.loc[gen_days["cal_date"] == trading_date, "pretrade_date"].iloc[0]
    gen_start = gen_days.iloc[0]["cal_date"]
    gen_raw = hx.fund_daily(etf=stk, start_date=gen_start, end_date=yesterday, adjust="front")
    gen_ohlc = gen_raw[["open", "high", "low", "close"]]
    print(f"end_date=yesterday({yesterday})，保留 trade_date 索引:")
    print(gen_ohlc.tail(3).to_string())
    normed = gen_ohlc / gen_ohlc.iloc[0]["close"]
    print()
    print("generate 整段除以首日 close（第 163 行）后 close.tail(3):")
    print(normed["close"].tail(3).round(6).to_string())


def demo_index_daily(hx) -> pd.Series:
    section("8 · index_daily · 1_2 基准（第 204 行）")
    benchmark = hx.index_daily(index_code="000300.SH", start_date=START, end_date=END)
    print("type ->", type(benchmark).__name__, "| name ->", benchmark.name)
    if benchmark.empty:
        print("（当前环境 index_daily 为空，需 token / 缓存；形状见 09 课）")
        # 稳定占位：与 09 课一致的真实片段，便于文档对齐
        benchmark = pd.Series(
            [-0.013045, -0.002379, -0.009249],
            index=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]),
            name="pct_chg",
        )
        benchmark.index.name = "trade_date"
        print("fallback 示例:")
    print(benchmark.head(3).to_string())
    return benchmark


def demo_analyzer(hx, benchmark: pd.Series) -> None:
    section("9 · analyzer · 1_2 绩效对比（第 208 行）")
    sample = benchmark.head(5).copy()
    if len(sample) < 3:
        sample = pd.Series(
            [-0.013045, -0.002379, -0.009249, 0.001, 0.002],
            index=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-08"]),
            name="pct_chg",
        )
        sample.index.name = "trade_date"
    pnl = sample.copy()
    pnl.iloc[0] = 0.015
    pnl.iloc[2] = 0.008
    print("pnl（策略日收益，来自 backtrader TimeReturn）head(3):")
    print(pnl.head(3).to_string())
    print()
    print("benchmark.head(3):")
    print(sample.head(3).to_string())

    stats = hx.analyzer(pnl, sample, strategy=None, fig_name=None)
    print()
    print("stats['strategy'] ->", _round_dict(stats["strategy"]))
    print("stats['benchmark'] ->", _round_dict(stats["benchmark"]))
    print("stats['figure'] ->", stats["figure"], "（fig_name 非空时写 PNG）")


def _round_dict(d: dict) -> dict:
    out = {}
    for k, v in d.items():
        if isinstance(v, float):
            out[k] = round(v, 6) if v == v else v
        else:
            out[k] = v
    return out


def main() -> None:
    utf8_stdout()
    helper, hx = load_hkcodex()
    demo_bootstrap(helper)
    _, trade_days_with_warmup = demo_get_trade_days(hx)
    demo_fund_daily(hx, trade_days_with_warmup)
    benchmark = demo_index_daily(hx)
    demo_analyzer(hx, benchmark)


if __name__ == "__main__":
    main()
