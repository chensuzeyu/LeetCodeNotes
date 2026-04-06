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
    # Windows：退出 TemporaryDirectory 前必须先 chdir 出该目录，否则 rmtree 报 WinError 32
    old_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as td:
        try:
            os.chdir(td)
            print("chdir 临时目录后 getcwd:", os.getcwd())
        finally:
            os.chdir(old_cwd)
    print("恢复后 getcwd:", os.getcwd())

    section("sys：argv / path / version / executable")
    print("sys.argv:", sys.argv)
    print("len(sys.path):", len(sys.path))
    print("sys.path[0]（脚本目录，用于 import 搜索起点）:", sys.path[0])
    fake = str(Path(__file__).resolve().parent / "_demo_sys_path_insert")
    sys.path.insert(0, fake)
    print("insert(0, ...) 后 path[0]:", sys.path[0])
    sys.path.pop(0)
    print("pop(0) 后恢复原 path[0]:", sys.path[0])
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
    proc_exit = subprocess.run(
        [sys.executable, "-c", "import sys; sys.exit(7)"],
        capture_output=True,
        text=True,
    )
    print("子进程 sys.exit(7) returncode:", proc_exit.returncode)
    try:
        subprocess.run(
            [sys.executable, "-c", "import sys; sys.exit(1)"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print("check=True 捕获 CalledProcessError returncode:", e.returncode)

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
        rm_dir = base / "rm_me"
        rm_dir.mkdir()
        (rm_dir / "x.txt").write_text("x", encoding="utf-8")
        shutil.rmtree(rm_dir)
        print("rmtree 后 rm_dir.exists():", rm_dir.exists())


if __name__ == "__main__":
    main()
