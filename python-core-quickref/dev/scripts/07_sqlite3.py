"""对应 07-sqlite3.md：sqlite3 占位符与 Row"""

from __future__ import annotations

import sqlite3

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("sqlite3：内存库、占位符、Row")
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    conn.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
    conn.execute("INSERT INTO users(name) VALUES (?)", ("Bob",))
    conn.commit()
    rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
    for row in rows:
        print(dict(row))
    conn.close()


if __name__ == "__main__":
    main()
