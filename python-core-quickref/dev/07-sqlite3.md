# 07 · sqlite3（单机嵌入式数据库）

完整演示：[scripts/07_sqlite3.py](scripts/07_sqlite3.py)  
运行：`python 07_sqlite3.py`（在 `dev/scripts` 目录）

本地缓存、小到中型工具、原型持久化：**零服务**即可用；SQL 与事务概念与其他 DB 相通。  
下文「预期输出」与脚本一致（见 [../README.md](../README.md) 维护约定）。

## 要点

| 用法 | 说明 |
|------|------|
| `sqlite3.connect(":memory:")` / `connect("app.db")` | 内存库或文件库 |
| `conn.execute(sql, params)` | **请用占位符** `?`，不要拼接字符串防注入 |
| `conn.commit()` | 写操作后提交 |
| `conn.row_factory = sqlite3.Row` | 行可按键名索引；`dict(row)` 转普通字典便于打印 |
| 上下文：`with conn:` | 自动 commit / rollback（按版本与用法约定） |

### 占位符

- 示例：`INSERT INTO users(name) VALUES (?)`，参数为 `("Ada",)` 元组。

**预期输出摘录**：

```text
{'id': 1, 'name': 'Ada'}
{'id': 2, 'name': 'Bob'}
```

## 官方文档

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
