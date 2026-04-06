# 03 · datetime / zoneinfo（时间与多时区）

完整演示：[scripts/03_datetime_zoneinfo.py](scripts/03_datetime_zoneinfo.py)  
运行：`python 03_datetime_zoneinfo.py`（在 `dev/scripts` 目录）

日志、任务调度、接口对接时经常要处理**本地时间 / UTC / 时区**；应用层优先用标准库，避免手写偏移。  
改脚本时请同步更新本文预期输出中的**时间戳**（见 [../README.md](../README.md) 维护约定）。

## datetime

| 类型 / 用法 | 说明 |
|-------------|------|
| `date` / `time` / `datetime` | 日期、一天内时间、日期+时间 |
| `datetime.now(tz=None)` | `tz` 为 `None` 时多为**本地**「意识模糊」时间；建议明确 `timezone.utc` 或 `ZoneInfo` |
| `datetime.fromisoformat(s)` | 解析 ISO 8601 常见形式（注意带 `Z` 时需替换或自行规范为 `+00:00`） |
| `timedelta` | 时长：`datetime + timedelta(days=2)` 等 |
| `timezone.utc` | 固定 UTC 偏移；简单场景够用 |

### 示例与预期形态

```python
utc_now = datetime.now(timezone.utc)
parsed = datetime.fromisoformat("2026-04-06T12:34:56+00:00")
```

**预期输出形态**（微秒与「今天」日期随运行时刻变化）：

```text
UTC now: 2026-04-06 ...+00:00
加 2 天: 2026-04-08 ...+00:00
fromisoformat: 2026-04-06 12:34:56+00:00
```

## zoneinfo（Python 3.9+）

| 用法 | 说明 |
|------|------|
| `ZoneInfo("Asia/Shanghai")` | IANA 时区名；依赖系统或 `tzdata` 包（Windows 可 `pip install tzdata`） |
| 带 tz 的 `datetime` | `astimezone(timezone.utc)` 等与 UTC 互转 |

若脚本中 `import` 失败，会打印降级提示（以终端为准）。

**预期输出摘录（成功时）**：

```text
Asia/Shanghai: 2026-06-01 12:00:00+08:00 -> UTC: 2026-06-01 04:00:00+00:00
today: 2026-04-06
```

## 官方文档

- [datetime](https://docs.python.org/3/library/datetime.html)  
- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html)
