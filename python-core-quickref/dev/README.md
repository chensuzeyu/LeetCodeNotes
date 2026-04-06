# Python 3 速查 · 日常开发

**与刷题分离**：脚本、小服务、批处理、测试打底用的**标准库**速查；算法题常用库见 [leetcode/README.md](../leetcode/README.md)。

目标：**覆盖日常 Python 脚本/小工程中最常碰到的标准库场景**（I/O、配置、进程、网络客户端、数据库、并发、测试、类型与数据类）。第三方（如 `requests`、`pytest`、`httpx`）不做全集，仅在个别文档中点到为止。

## 怎么用

```bash
cd python-core-quickref/dev/scripts
python run_all.py
```

或单课：`python 04_csv_config.py`

要求：**Python 3.9+**（`tomllib` 仅在 **3.11+** 有标准库实现，见 `04`）。Windows 终端乱码见 [上层 README](../README.md)。

## 文档索引

| 文档 | 演示脚本 | 内容 |
|------|----------|------|
| [01-json-re-pathlib.md](01-json-re-pathlib.md) | [scripts/01_json_re_pathlib.py](scripts/01_json_re_pathlib.py) | `json`、`re`、`pathlib` |
| [02-logging-argparse.md](02-logging-argparse.md) | [scripts/02_logging_argparse.py](scripts/02_logging_argparse.py) | `logging`、`argparse` |
| [03-datetime-zoneinfo.md](03-datetime-zoneinfo.md) | [scripts/03_datetime_zoneinfo.py](scripts/03_datetime_zoneinfo.py) | `datetime`、`zoneinfo` |
| [04-csv-config.md](04-csv-config.md) | [scripts/04_csv_config.py](scripts/04_csv_config.py) | `csv`、`configparser`、`tomllib`（3.11+） |
| [05-os-sys-subprocess-shutil.md](05-os-sys-subprocess-shutil.md) | [scripts/05_os_sys_subprocess_shutil.py](scripts/05_os_sys_subprocess_shutil.py) | `os`、`sys`、`subprocess`、`shutil` |
| [06-urllib.md](06-urllib.md) | [scripts/06_urllib.py](scripts/06_urllib.py) | `urllib.parse`、`urllib.request` |
| [07-sqlite3.md](07-sqlite3.md) | [scripts/07_sqlite3.py](scripts/07_sqlite3.py) | `sqlite3` |
| [08-concurrent-threading.md](08-concurrent-threading.md) | [scripts/08_concurrent_threading.py](scripts/08_concurrent_threading.py) | `concurrent.futures`、`threading` |
| [09-unittest.md](09-unittest.md) | [scripts/09_unittest.py](scripts/09_unittest.py) | `unittest` |
| [10-dataclasses-typing.md](10-dataclasses-typing.md) | [scripts/10_dataclasses_typing.py](scripts/10_dataclasses_typing.py) | `dataclasses`、`typing` |

## 维护

新增日常向主题：在本目录加 `0x-*.md` 与 `scripts/0x_*.py`，并更新 `scripts/run_all.py` 的 `demos`。
