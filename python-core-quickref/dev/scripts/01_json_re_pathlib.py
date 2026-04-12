"""对应 01-json-re-pathlib.md：json、re、pathlib 脚本常用写法"""

from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("json：loads / dumps")
    raw = '{"x": 1, "msg": "你好"}'
    obj = json.loads(raw)
    print("loads ->", obj)
    out = json.dumps(obj, ensure_ascii=False, indent=2)
    print("dumps(ensure_ascii=False, indent=2):\n", out)

    section("re：findall / search / compile")
    s = "abc 12 def 345"
    print("digits:", re.findall(r"\d+", s))
    m = re.search(r"def\s+(\d+)", s)
    print("search 分组:", m.group(1) if m else None)
    m_head = re.match(r"\d+", s)
    print("match 从开头（首字符非数字）:", m_head)
    m_ok = re.match(r"abc", s)
    print("match abc:", m_ok.group(0) if m_ok else None)
    pat = re.compile(r"[a-z]+")
    print("compile.findall ->", pat.findall(s))

    section("pathlib：Path、read_text、write_text、/ 拼接")
    rel = Path("a") / "b" / "c.txt"
    print("relative path ->", rel)
    print("relative parts ->", rel.parts)
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        cfg = base / "conf" / "app.json"
        cfg.parent.mkdir(parents=True, exist_ok=True)
        print("base / 'conf' / 'app.json' ->", cfg)
        cfg.write_text('{"ok": true}\n', encoding="utf-8")
        print("写入:", cfg)
        print("read_text ->", repr(cfg.read_text(encoding="utf-8")))
        print("cwd =", Path.cwd())


if __name__ == "__main__":
    main()
