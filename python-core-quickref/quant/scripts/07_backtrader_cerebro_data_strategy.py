"""对应 07-backtrader-cerebro-data-strategy.md：PandasData、Cerebro、Strategy、next。"""

from __future__ import annotations

import backtrader as bt
import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


class DemoStrategy(bt.Strategy):
    def __init__(self) -> None:
        self.closes: list[float] = []
        print("Strategy.__init__ -> data feeds:", len(self.datas))

    def next(self) -> None:
        dt = self.datas[0].datetime.date(0).strftime("%Y-%m-%d")
        close = float(self.datas[0].close[0])
        self.closes.append(round(close, 2))
        print("next ->", dt, round(close, 2))


def main() -> None:
    utf8_stdout()

    data = pd.DataFrame(
        {
            "open": [10.0, 10.2, 10.4],
            "high": [10.1, 10.3, 10.5],
            "low": [9.9, 10.1, 10.3],
            "close": [10.05, 10.25, 10.45],
        },
        index=pd.to_datetime(["2024-01-08", "2024-01-09", "2024-01-10"]),
    )

    section("PandasData：把 DataFrame 喂给回测系统")
    print("input rows ->", len(data))
    print("input index ->", data.index.strftime("%Y-%m-%d").tolist())

    section("Cerebro / adddata / addstrategy / run")
    cerebro = bt.Cerebro()
    datafeed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(datafeed, name="demo_etf")
    cerebro.addstrategy(DemoStrategy)
    result = cerebro.run()
    print("result strategy count ->", len(result))
    print("closes seen ->", result[0].closes)


if __name__ == "__main__":
    main()
