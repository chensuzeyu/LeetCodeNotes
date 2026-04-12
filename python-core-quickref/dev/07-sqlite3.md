# 07 · sqlite3（单机嵌入式数据库）

完整演示：[scripts/07_sqlite3.py](scripts/07_sqlite3.py)  
运行：`python3 07_sqlite3.py`（在 `dev/scripts` 目录）

本地缓存、小到中型工具、原型持久化时，`sqlite3` 可以做到零服务启动。  
下文各「输入代码 / 输出结果」与脚本逐段对应（见 [../README.md](../README.md) 维护约定）。

## 要点

| 用法 | 说明 |
|------|------|
| `sqlite3.connect(":memory:")` / `connect("app.db")` | 内存库或文件库 |
| `conn.execute(sql, params)` | 用 `?` 占位符传参，避免拼接 SQL |
| `conn.commit()` | 写操作后提交 |
| `conn.row_factory = sqlite3.Row` | 行可按键名索引；`dict(row)` 便于打印 |
| `with conn:` | 让连接生命周期更清晰 |

### 占位符、`Row` 与 `fetchall()`

- SQL 参数要通过 `?` 占位符传进去，不要自己拼字符串。
- `sqlite3.Row` 让结果既能按位置取，也能按列名取，调试和打印会舒服很多。
- `:memory:` 只在当前连接活着时存在；一断开，数据就没了。

**输入代码**：

```python
with sqlite3.connect(":memory:") as conn:
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    conn.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
    conn.execute("INSERT INTO users(name) VALUES (?)", ("Bob",))
    conn.commit()
    rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
```

**输出结果**（`stdout`）：

```text
{'id': 1, 'name': 'Ada'}
{'id': 2, 'name': 'Bob'}
```

## 官方文档

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
