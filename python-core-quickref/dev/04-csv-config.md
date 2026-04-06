# 04 · csv / configparser / tomllib（表格与配置）

完整演示：`scripts/04_csv_config.py`  
运行：`python 04_csv_config.py`（在 `dev/scripts` 目录下）

**ETL 小工具、批处理、服务读本地配置**三类场景极常见。

## csv

| 用法 | 说明 |
|------|------|
| `csv.reader(f)` / `csv.writer(f)` | 行迭代写行；注意 `open(..., newline="")` 推荐由文档说明 |
| `csv.DictReader` / `DictWriter` | 表头 ↔ 字典，列名更清晰 |

## configparser（INI）

| 用法 | 说明 |
|------|------|
| `ConfigParser()` | 解析 `key=value` 分段 INI |
| `read(["a.ini", "b.ini"])` | 多文件后者可覆盖前者（按设计） |
| `get(section, key)` / `getint` / `getboolean` | 带类型转换 |

## tomllib（标准库 TOML，Python 3.11+）

| 用法 | 说明 |
|------|------|
| `tomllib.loads(s)` / `tomllib.load(f)` | **只读**；`f` 须二进制打开 `rb` |
| 3.9–3.10 | 标准库无 `tomllib`；项目中常用第三方 `tomli`（只读）或 `toml` |

## 官方文档

- [csv](https://docs.python.org/3/library/csv.html)  
- [configparser](https://docs.python.org/3/library/configparser.html)  
- [tomllib](https://docs.python.org/3/library/tomllib.html)
