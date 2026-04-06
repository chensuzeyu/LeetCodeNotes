"""依次运行本目录全部「日常开发向」演示脚本。"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from _io_util import utf8_stdout


def load_and_run(name: str) -> None:
    path = Path(__file__).with_name(f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载: {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    run_main = getattr(mod, "main")
    run_main()


def main() -> None:
    utf8_stdout()
    script_dir = str(Path(__file__).resolve().parent)
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

    demos = [
        "01_json_re_pathlib",
    ]
    print("Python:", sys.version.split()[0])
    print("【日常开发速查】工作目录:", Path(__file__).resolve().parent)
    for d in demos:
        print("\n" + "#" * 60)
        print("# 运行:", d + ".py")
        print("#" * 60)
        load_and_run(d)
    print("\n日常向演示全部结束。（刷题见 ../../leetcode/scripts/run_all.py）")


if __name__ == "__main__":
    main()
