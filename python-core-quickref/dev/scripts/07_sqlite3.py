"""对应 07-sqlite3.md：sqlite3 占位符与 Row"""

from __future__ import annotations

import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("sqlite3：内存库、文件库、占位符、Row、with conn 提交")
    with closing(sqlite3.connect(":memory:")) as conn:
        conn.row_factory = sqlite3.Row
        with conn:
            conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
            conn.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
            conn.execute("INSERT INTO users(name) VALUES (?)", ("Bob",))
        rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
        for row in rows:
            print(dict(row))
        print("首行按键访问 row['name'] ->", rows[0]["name"])

    with tempfile.TemporaryDirectory() as td:
        db_path = Path(td) / "app.db"
        with closing(sqlite3.connect(db_path)) as conn:
            conn.row_factory = sqlite3.Row
            with conn:
                conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
                conn.execute("INSERT INTO users(name) VALUES (?)", ("Cara",))
            row = conn.execute("SELECT id, name FROM users WHERE name = ?", ("Cara",)).fetchone()
            row_dict = dict(row) if row is not None else None
        print("file db exists ->", db_path.exists())
        print("file row ->", row_dict)


if __name__ == "__main__":
    main()
