# 07 · backtrader 的 Cerebro / Data Feed / Strategy

完整演示：[scripts/07_backtrader_cerebro_data_strategy.py](scripts/07_backtrader_cerebro_data_strategy.py)  
运行：`python3 07_backtrader_cerebro_data_strategy.py`

偏**回测系统的对象关系**：`DataFrame` 怎么喂给 `PandasData`，`PandasData` 怎么交给 `Cerebro`，`Cerebro` 怎么驱动 `Strategy.next()`。  
先把对象关系看懂，再去看 `1_2_ETF轮动_回测.py` 会轻松很多。

## `PandasData`

| 要点 | 说明 |
|------|------|
| 输入 | 一个带时间索引的 OHLC `DataFrame` |
| 作用 | 把 `pandas` 行情表包装成 `backtrader` 可读的数据源 |

**输入代码**：

```python
data = pd.DataFrame(
    {
        "open": [10.0, 10.2, 10.4],
        "high": [10.1, 10.3, 10.5],
        "low": [9.9, 10.1, 10.3],
        "close": [10.05, 10.25, 10.45],
    },
    index=pd.to_datetime(["2024-01-08", "2024-01-09", "2024-01-10"]),
)
```

**输出结果**：

```text
input rows -> 3
input index -> ['2024-01-08', '2024-01-09', '2024-01-10']
```

## `Cerebro` / `Strategy`

| 用法 | 说明 |
|------|------|
| `cerebro.adddata(...)` | 注册数据源 |
| `cerebro.addstrategy(...)` | 注册策略类 |
| `cerebro.run()` | 真正开始逐 bar 推进 |

**输入代码**：

```python
cerebro = bt.Cerebro()
datafeed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(datafeed, name="demo_etf")
cerebro.addstrategy(DemoStrategy)
result = cerebro.run()
```

**输出结果**：

```text
Strategy.__init__ -> data feeds: 1
next -> 2024-01-08 10.05
next -> 2024-01-09 10.25
next -> 2024-01-10 10.45
result strategy count -> 1
closes seen -> [10.05, 10.25, 10.45]
```

**注意点**：`__init__` 更像“策略启动时的初始化”，真正按时间一根一根走行情的是 `next()`；读回测代码时不要把两者混了。

## 官方文档

- [Backtrader Quickstart](https://www.backtrader.com/docu/quickstart/quickstart/)
