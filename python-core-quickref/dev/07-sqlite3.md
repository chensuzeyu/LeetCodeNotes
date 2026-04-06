# 07 · sqlite3（单机嵌入式数据库）

完整演示：`scripts/07_sqlite3.py`  
运行：`python 07_sqlite3.py`（在 `dev/scripts` 目录下）

本地缓存、小到中型工具、原型持久化：**零服务**即可用；SQL 与事务概念与其他 DB 相通。

## 要点

| 用法 | 说明 |
|------|------|
| `sqlite3.connect(":memory:")` / `connect("app.db")` | 内存库或文件库 |
| `conn.execute(sql, params)` | **请用占位符** `?`，不要拼接字符串防注入 |
| `conn.commit()` | 写操作后提交 |
| `conn.row_factory = sqlite3.Row` | 按列名索引行 |
| 上下文：`with conn:` | 自动 commit / rollback（按版本与用法约定） |

## 官方文档

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
