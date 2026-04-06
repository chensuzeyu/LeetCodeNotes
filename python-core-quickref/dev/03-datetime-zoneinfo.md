# 03 · datetime / zoneinfo（时间与多时区）

完整演示：[scripts/03_datetime_zoneinfo.py](scripts/03_datetime_zoneinfo.py)  
运行：`python 03_datetime_zoneinfo.py`（在 `dev/scripts` 目录）

日志、任务调度、接口对接时经常要处理**本地时间 / UTC / 时区**；应用层优先用标准库，避免手写偏移。  
下文各「输入输出示例」与脚本 **一一对应**；含**当前时刻**的行会因运行时间变化（见 [../README.md](../README.md) 维护约定）。

## datetime

| 类型 / 用法 | 说明 |
|-------------|------|
| `date` / `time` / `datetime` | 日期、一天内时间、日期+时间 |
| `datetime.now(tz=None)` | `tz` 为 `None` 时多为**本地**「意识模糊」时间；建议明确 `timezone.utc` 或 `ZoneInfo` |
| `datetime.fromisoformat(s)` | 解析 ISO 8601 常见形式（注意带 `Z` 时需替换或自行规范为 `+00:00`） |
| `timedelta` | 时长：`datetime + timedelta(days=2)` 等 |
| `timezone.utc` | 固定 UTC 偏移；简单场景够用 |

**输入输出示例**

**输入**（`03_datetime_zoneinfo.py`）：

```python
time(14, 30)
datetime.now()
utc_now = datetime.now(timezone.utc)
utc_now + timedelta(days=2)
s = "2026-04-06T12:34:56+00:00"
datetime.fromisoformat(s)
```

**输出**（`stdout`；`datetime.now()` 与 `UTC now` 的微秒、日期随运行时刻变化；`加 2 天` 为 `utc_now` 的日期 +2 天）：

```text
time(14, 30): 14:30:00
datetime.now()（未带 tz，本地语义依环境）: 2026-04-06 21:36:30.323573
UTC now: 2026-04-06 13:36:30.324576+00:00
加 2 天: 2026-04-08 13:36:30.324576+00:00
fromisoformat: 2026-04-06 12:34:56+00:00
```

（上表为一次真实运行样例；你本地复现时仅前两行与 `UTC now`/`加 2 天` 中的时间戳会不同。）

## zoneinfo（Python 3.9+）

| 用法 | 说明 |
|------|------|
| `ZoneInfo("Asia/Shanghai")` | IANA 时区名；依赖系统或 `tzdata` 包（Windows 可 `pip install tzdata`） |
| 带 tz 的 `datetime` | `astimezone(timezone.utc)` 等与 UTC 互转 |

若脚本中 `import` 失败，会打印降级提示（以终端为准）。

**输入输出示例（成功）**

**输入**（`03_datetime_zoneinfo.py`）：

```python
from zoneinfo import ZoneInfo
sh = ZoneInfo("Asia/Shanghai")
localish = datetime(2026, 6, 1, 12, 0, 0, tzinfo=sh)
localish.astimezone(timezone.utc)
date.today()
```

**输出**（`stdout`；`today` 为运行日）：

```text
Asia/Shanghai: 2026-06-01 12:00:00+08:00 -> UTC: 2026-06-01 04:00:00+00:00
today: 2026-04-06
```

**输入输出示例（import 失败时）**

**输入**：同上，但系统无 IANA 数据。

**输出**（`stdout`，文案与 `exc` 因环境略异）：

```text
(跳过或降级) <异常类型> <异常信息>
提示：Windows 可 pip install tzdata 以提供 IANA 数据。
```

## 官方文档

- [datetime](https://docs.python.org/3/library/datetime.html)  
- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html)
