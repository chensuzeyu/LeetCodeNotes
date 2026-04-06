# 04 · csv / configparser / tomllib（表格与配置）

完整演示：[scripts/04_csv_config.py](scripts/04_csv_config.py)  
运行：`python 04_csv_config.py`（在 `dev/scripts` 目录）

**ETL 小工具、批处理、服务读本地配置**三类场景极常见。  
下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## csv

| 用法 | 说明 |
|------|------|
| `csv.reader(f)` / `csv.writer(f)` | 行迭代写行；**写磁盘**时 `open(..., newline="")` 避免多余 `\r\r\n` |
| `csv.DictReader` / `DictWriter` | 表头 ↔ 字典，`fieldnames` 与表头行一致 |

### `DictReader` 读回的值

- **单元格一律是字符串**；需要整数要自己 `int(row["score"])`。

**预期输出摘录**（`DictWriter` 默认 `\r\n` 行尾，显示时可能看到 `␤` 或裸 `\r`）：

```text
name,score
Ann,92
Bob,88
read back: [{'name': 'Ann', 'score': '92'}, {'name': 'Bob', 'score': '88'}]
```

## configparser（INI）

| 用法 | 说明 |
|------|------|
| `ConfigParser()` | 解析 `key=value` 分段 INI |
| `read(["a.ini", "b.ini"])` | 多文件后者可覆盖前者（按设计） |
| `get(section, key)` / `getint` / `getboolean` | 带类型转换 |

**预期输出摘录**：

```text
getboolean(app, debug) = True
getint(app, port)      = 8080
read file [db].url = sqlite:///./app.db
```

## tomllib（标准库 TOML，Python 3.11+）

| 用法 | 说明 |
|------|------|
| `tomllib.loads(s)` / `tomllib.load(f)` | **只读**；`load` 时 `f` 须**二进制**打开 `rb` |
| 3.9–3.10 | 标准库无 `tomllib`；常用第三方 `tomli`（只读）或 `toml` |

**预期输出**：3.11+ 为 `tomllib.loads -> {'title': 'demo', 'nested': {'count': 3}}`；低版本为脚本中的提示行（以本机 `python --version` 为准）。

## 官方文档

- [csv](https://docs.python.org/3/library/csv.html)  
- [configparser](https://docs.python.org/3/library/configparser.html)  
- [tomllib](https://docs.python.org/3/library/tomllib.html)
