"""对应 05-os-sys-subprocess-shutil.md：os、sys、subprocess、shutil"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
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
    section("os.environ：读取（勿打印含密钥的完整 environ）")
    path_preview = os.environ.get("PATH", "")
    print("PATH 前 80 字:", (path_preview[:80] + "…") if len(path_preview) > 80 else path_preview)
    print("getcwd:", os.getcwd())

    section("sys：argv / version / executable")
    print("sys.version:", sys.version.split()[0])
    print("sys.executable:", sys.executable)

    section("subprocess.run：调当前解释器执行短代码")
    proc = subprocess.run(
        [sys.executable, "-c", "print('subprocess ok')"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("stdout:", proc.stdout.strip())

    section("shutil：copy2 / move（临时目录内）")
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        src = base / "a.txt"
        src.write_text("hello", encoding="utf-8")
        dst = base / "b" / "a.txt"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print("copy2 后 exists:", dst.is_file(), "内容:", repr(dst.read_text(encoding="utf-8")))
        moved = base / "c.txt"
        shutil.move(dst, moved)
        print("move 后:", moved.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
