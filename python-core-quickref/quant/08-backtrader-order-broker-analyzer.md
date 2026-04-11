# 08 · backtrader 的下单 / broker / analyzer

完整演示：[scripts/08_backtrader_order_broker_analyzer.py](scripts/08_backtrader_order_broker_analyzer.py)  
运行：`python3 08_backtrader_order_broker_analyzer.py`

偏**回测里最容易把人绕晕的那一层**：下单不是立即成交，成交有回调，盈亏有回调，收益序列还要从 analyzer 里拿。  
这一节读完，再回头看 `notify_order` / `notify_trade` 会顺很多。

## broker

| 用法 | 说明 |
|------|------|
| `cerebro.broker.setcash(1000.0)` | 设置初始资金 |
| `broker.getcash()` / `broker.getvalue()` | 看现金和总资产 |

**输入代码**：

```python
cerebro = bt.Cerebro()
cerebro.broker.setcash(1000.0)
```

**输出结果**：

```text
start cash -> 1000.0
```

## 下单 / 成交 / 回调

| 用法 | 说明 |
|------|------|
| `order_target_size(target=10)` | 调整目标仓位 |
| `close()` | 平仓 |
| `notify_order` | 订单成交时回调 |
| `notify_trade` | 一笔交易闭合时回调 |

**输入代码**：

```python
if len(self) == 1 and not self.position:
    self.order_target_size(target=10)
elif len(self) == 3 and self.position:
    self.close()
```

**输出结果**：

```text
next -> 2024-01-08 order_target_size(10)
notify_order -> BUY price=11.00 size=10
next -> 2024-01-10 close()
notify_order -> SELL price=11.50 size=-10
notify_trade -> pnl 5.0
```

**注意点**：你在 `2024-01-08` 发出买单，但真正成交价是第二天开盘价 `11.00`；这就是为什么回测里“发单时点”和“成交时点”必须分开看。

## `TimeReturn`

| 用法 | 说明 |
|------|------|
| `cerebro.addanalyzer(bt.analyzers.TimeReturn, _name="_TimeReturn")` | 挂收益分析器 |
| `get_analysis()` | 取回收益序列 |

**输入代码**：

```python
cerebro.addanalyzer(bt.analyzers.TimeReturn, _name="_TimeReturn")
pnl = strat.analyzers._TimeReturn.get_analysis()
```

**输出结果**：

```text
final cash -> 1005.0
final value -> 1005.0
logged_orders -> ['BUY price=11.00 size=10', 'SELL price=11.50 size=-10']
logged_trades -> [5.0]
TimeReturn -> {'2024-01-08': 0.0, '2024-01-09': 0.0, '2024-01-10': 0.01, '2024-01-11': -0.00495}
```

## 官方文档

- [Backtrader Analyzer](https://www.backtrader.com/docu/analyzers/analyzers/)
