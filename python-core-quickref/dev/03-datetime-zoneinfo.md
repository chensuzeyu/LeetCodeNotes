# 03 · datetime / zoneinfo（时间与多时区）

完整演示：`scripts/03_datetime_zoneinfo.py`  
运行：`python 03_datetime_zoneinfo.py`（在 `dev/scripts` 目录下）

日志、任务调度、接口对接时经常要处理**本地时间 / UTC / 时区**；应用层优先用标准库，避免手写偏移。

## datetime

| 类型 / 用法 | 说明 |
|-------------|------|
| `date` / `time` / `datetime` | 日期、一天内时间、日期+时间 |
| `datetime.now(tz=None)` | `tz` 为 `None` 时多为**本地**「意识模糊」时间；建议明确 `timezone.utc` 或 `ZoneInfo` |
| `datetime.fromisoformat(s)` | 解析 ISO 8601 常见形式（注意带 `Z` 时需替换或自行规范） |
| `timedelta` | 时长：`+`、`-`、`*` 整数 |
| `timezone.utc` | 固定 UTC 偏移；简单场景够用 |

## zoneinfo（Python 3.9+）

| 用法 | 说明 |
|------|------|
| `ZoneInfo("Asia/Shanghai")` | IANA 时区名；依赖系统 tzdata（Windows 可装 `tzdata` 包） |
| 带 tz 的 `datetime` | 与 UTC 互转、比较时更不容易踩夏令时坑 |

## 官方文档

- [datetime](https://docs.python.org/3/library/datetime.html)  
- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html)
