"""对应 08-backtrader-order-broker-analyzer.md：下单、broker、notify_order、notify_trade、TimeReturn。"""

from __future__ import annotations

import backtrader as bt
import pandas as pd

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


class OrderDemoStrategy(bt.Strategy):
    def __init__(self) -> None:
        self.logged_orders: list[str] = []
        self.logged_trades: list[float] = []

    def next(self) -> None:
        dt = self.datas[0].datetime.date(0).strftime("%Y-%m-%d")
        if len(self) == 1 and not self.position:
            print("next ->", dt, "order_target_size(10)")
            self.order_target_size(target=10)
        elif len(self) == 3 and self.position:
            print("next ->", dt, "close()")
            self.close()

    def notify_order(self, order: bt.Order) -> None:
        if order.status == order.Completed:
            side = "BUY" if order.isbuy() else "SELL"
            msg = f"{side} price={order.executed.price:.2f} size={order.executed.size:.0f}"
            self.logged_orders.append(msg)
            print("notify_order ->", msg)

    def notify_trade(self, trade: bt.Trade) -> None:
        if trade.isclosed:
            pnl = round(float(trade.pnl), 2)
            self.logged_trades.append(pnl)
            print("notify_trade -> pnl", pnl)


def main() -> None:
    utf8_stdout()

    data = pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0, 11.5],
            "high": [10.2, 11.2, 12.2, 11.7],
            "low": [9.8, 10.8, 11.8, 11.3],
            "close": [10.0, 11.0, 12.0, 11.5],
        },
        index=pd.to_datetime(["2024-01-08", "2024-01-09", "2024-01-10", "2024-01-11"]),
    )

    section("broker：初始资金 / 数据输入")
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(1000.0)
    print("start cash ->", cerebro.broker.getcash())

    section("下单 / 成交 / analyzer")
    cerebro.adddata(bt.feeds.PandasData(dataname=data), name="demo_etf")
    cerebro.addstrategy(OrderDemoStrategy)
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name="_TimeReturn")
    result = cerebro.run()
    strat = result[0]
    pnl = strat.analyzers._TimeReturn.get_analysis()
    print("final cash ->", round(float(cerebro.broker.getcash()), 2))
    print("final value ->", round(float(cerebro.broker.getvalue()), 2))
    print("logged_orders ->", strat.logged_orders)
    print("logged_trades ->", strat.logged_trades)
    print("TimeReturn ->", {k.strftime('%Y-%m-%d'): round(float(v), 6) for k, v in pnl.items()})


if __name__ == "__main__":
    main()
