# Python 3 核心速查（分册）

本仓库将速查拆成两册，避免刷题与日常开发混在同一目录里：

| 分册 | 路径 | 用途 |
|------|------|------|
| **刷题** | [leetcode/README.md](leetcode/README.md) | 力扣 / 竞赛常见：`heapq`、`bisect`、`Counter`、记忆化、位运算等（`01`～`07`） |
| **日常开发** | [dev/README.md](dev/README.md) | 脚本与工程打底：`01`～`11`（含 `random`/`copy` 等） |

## 快速运行

**刷题向（连跑 01～07）：**

```bash
cd python-core-quickref/leetcode/scripts
python run_all.py
```

**日常向：**

```bash
cd python-core-quickref/dev/scripts
python run_all.py
```

环境：**Python 3.9+**。Windows 下若中文乱码，可先 `chcp 65001` 或设置 `PYTHONIOENCODING=utf-8`。

## 维护约定

- 刷题新增：只动 `leetcode/` 与 `leetcode/scripts/run_all.py`。  
- 日常新增：只动 `dev/` 与 `dev/scripts/run_all.py`。  
- 两套 scripts 各自带一份 `_io_util.py`，互不依赖，避免跨目录 import。

---

*与本仓库根目录 [README.md](../README.md) 中的 Python 3 说明一致。*
