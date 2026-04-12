# 03 · datetime / zoneinfo（时间与多时区）

完整演示：[scripts/03_datetime_zoneinfo.py](scripts/03_datetime_zoneinfo.py)  
运行：`python3 03_datetime_zoneinfo.py`（在 `dev/scripts` 目录）

日志、任务调度、接口对接时经常要处理**本地时间 / UTC / 时区**；应用层优先用标准库，避免手写偏移。  
下文各「输入代码 / 输出结果」与脚本逐段对应；含当前时刻或运行日期的片段用 `<NOW_LOCAL>`、`<NOW_UTC>`、`<TODAY>` 表示（见 [../README.md](../README.md) 占位规则）。

## datetime

| 类型 / 用法 | 说明 |
|-------------|------|
| `date` / `time` / `datetime` | 日期、一天内时间、日期+时间 |
| `datetime.now(tz=None)` | `tz=None` 时多为本地“意识模糊”时间 |
| `datetime.fromisoformat(s)` | 解析 ISO 8601 常见形式 |
| `timedelta` | 时长运算：`datetime + timedelta(days=2)` |
| `timezone.utc` | 固定 UTC 偏移；简单场景够用 |

### `time(...)` / `datetime.now(...)` / `timedelta` / `fromisoformat`

- `datetime.now()` 不带 `tz` 时通常是“naive datetime”，适合本地展示，不适合直接跨时区比较。
- `timedelta(days=2)` 是加“持续时长”，不是单纯把日期字符串里的天数改一改。

**输入代码**：

```python
time(14, 30)
datetime.now()
utc_now = datetime.now(timezone.utc)
utc_now + timedelta(days=2)

s = "2026-04-06T12:34:56+00:00"
datetime.fromisoformat(s)
```

**输出结果**（`stdout`）：

```text
time(14, 30): 14:30:00
datetime.now()（未带 tz，本地语义依环境）: <NOW_LOCAL>
UTC now: <NOW_UTC>
加 2 天: <NOW_UTC_PLUS_2D>
fromisoformat: 2026-04-06 12:34:56+00:00
```

## zoneinfo（Python 3.9+）

| 用法 | 说明 |
|------|------|
| `ZoneInfo("Asia/Shanghai")` | IANA 时区名；依赖系统或 `tzdata` |
| `astimezone(timezone.utc)` | 带时区时间与 UTC 互转 |

### `ZoneInfo(...)` 与时区转换

- `astimezone(...)` 的前提是原始 `datetime` 本身带时区；否则你很难知道“它当前到底代表哪个时区的时间”。
- `ZoneInfo("Asia/Shanghai")` 这种名字来自 IANA 时区数据库，不是随便写的任意字符串。

**输入代码**：

```python
from zoneinfo import ZoneInfo

sh = ZoneInfo("Asia/Shanghai")
localish = datetime(2026, 6, 1, 12, 0, 0, tzinfo=sh)
localish.astimezone(timezone.utc)
date.today()
```

**输出结果**（成功时）：

```text
Asia/Shanghai: 2026-06-01 12:00:00+08:00 -> UTC: 2026-06-01 04:00:00+00:00
today: <TODAY>
```

**输出结果**（无 IANA 时区数据时）：

```text
(跳过或降级) <EXC_TYPE> <EXC_MSG>
提示：Windows 可 pip install tzdata 以提供 IANA 数据。
today: <TODAY>
```

## 官方文档

- [datetime](https://docs.python.org/3/library/datetime.html)  
- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html)
