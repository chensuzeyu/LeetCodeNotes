# 力扣 Hot 100 完整学习路线

> 全覆盖版 · 约 18–24 周 · 每天 1–2 小时
>
> **语言：** 本仓库刷题路线与笔记中的「核心代码」一律采用 **Python 3**（类型标注等按 Python 3.9+ 习惯书写）。

---

## 目录

- [Python 3 核心速查（刷题 / 日常分册）](python-core-quickref/README.md)
- [第一阶段 · 基础数据结构](#第一阶段--基础数据结构4-5-周--29-题)
- [第二阶段 · 滑动窗口 & 二分查找 & 前缀和](#第二阶段--滑动窗口--二分查找--前缀和2-3-周--16-题)
- [第三阶段 · 树 & 图 & 矩阵](#第三阶段--树--图--矩阵3-4-周--28-题)
- [第四阶段 · 动态规划](#第四阶段--动态规划4-5-周--25-题)
- [第五阶段 · 回溯 & 高级数据结构](#第五阶段--回溯--高级数据结构3-4-周--15-题)
- [第六阶段 · 贪心 & 技巧](#第六阶段--贪心--技巧1-2-周--9-题)
- [学习方法](#学习方法)
- [仓库目录结构](#仓库目录结构)
- [笔记模板](#笔记模板)
- [从力扣页面提取原题文案](#从力扣页面提取原题文案)

---

## 仓库目录结构

```
LeetCodeNote/
├── README.md
├── python-core-quickref/       # Python 3 速查：刷题（leetcode）与日常（dev）分册
│   ├── README.md
│   ├── leetcode/               # 力扣/竞赛常用 API（01～07 + scripts）
│   └── dev/                    # 日常脚本向（01-json… + scripts）
├── scripts/
│   └── extract_lc_cn_meta.py   # 从力扣 CN 题目页 HTML 提取 meta 中的原题摘要（可复用）
└── notes/
    └── 第一阶段-基础数据结构/
        └── 数组与双指针/
            ├── 001-两数之和.md
            ├── 026-删除有序数组中的重复项.md
            └── 283-移动零.md
```

---

## 第一阶段 · 基础数据结构（4-5 周 · 29 题）

> 从最简单的数组、链表、哈希表入手，建立信心，掌握基础思维。

### 数组 & 双指针

本地笔记目录：`notes/第一阶段-基础数据结构/数组与双指针/`（题号文件名：`题号-题目简称.md`，全中文路径）

| 题号 | 题目 | 难度 | 链接 | 笔记 |
|:----:|------|:----:|------|------|
| 1 | 两数之和 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/two-sum/) | [笔记](notes/第一阶段-基础数据结构/数组与双指针/001-两数之和.md) |
| 26 | 删除有序数组中的重复项 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) | [笔记](notes/第一阶段-基础数据结构/数组与双指针/026-删除有序数组中的重复项.md) |
| 283 | 移动零 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/move-zeroes/) | [笔记](notes/第一阶段-基础数据结构/数组与双指针/283-移动零.md) |
| 75 | 颜色分类 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/sort-colors/) | — |
| 167 | 两数之和 II（输入有序数组） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | — |
| 11 | 盛最多水的容器 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/container-with-most-water/) | — |
| 15 | 三数之和 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/3sum/) | — |

**核心思路：** 双指针从两端向中间收缩，通过有序性减少枚举量，时间复杂度从 O(n²) 降到 O(n)。75 题是三路快排的应用，left/mid/right 三指针同时维护三个区间。

---

### 哈希表

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 242 | 有效的字母异位词 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/valid-anagram/) |
| 49 | 字母异位词分组 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/group-anagrams/) |
| 128 | 最长连续序列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-consecutive-sequence/) |

**核心思路：** 用哈希表把"查找"从 O(n) 降到 O(1)，以空间换时间。

---

### 链表

> ⚠️ 链表是 Hot 100 出现频次极高的结构，共 9 题，务必全部掌握。

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 206 | 反转链表 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/reverse-linked-list/) |
| 21 | 合并两个有序链表 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/merge-two-sorted-lists/) |
| 141 | 环形链表（判断是否有环） | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/linked-list-cycle/) |
| 876 | 链表的中间节点 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/middle-of-the-linked-list/) |
| 160 | 相交链表 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/intersection-of-two-linked-lists/) |
| 234 | 回文链表 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/palindrome-linked-list/) |
| 19 | 删除链表的倒数第 N 个节点 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) |
| 142 | 环形链表 II（找入环点） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/linked-list-cycle-ii/) |
| 148 | 排序链表 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/sort-list/) |

**核心思路：**
- 快慢指针是链表的灵魂——找中点、判环、找倒数第 N 个节点，全靠它
- 142 找入环点：快慢指针相遇后，一个指针回到 head，两者同速前进，再次相遇即入口
- 160 相交链表：两指针分别走完两条链表后换头，走相同步数必在交点相遇
- 148 排序链表：归并排序，用快慢指针找中点，递归拆分再合并

---

### 栈 & 单调栈

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 20 | 有效的括号 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/valid-parentheses/) |
| 155 | 最小栈 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/min-stack/) |
| 232 | 用栈实现队列 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/implement-queue-using-stacks/) |
| 150 | 逆波兰表达式求值 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) |
| 739 | 每日温度 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/daily-temperatures/) |
| 84 | 柱状图中最大的矩形 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/largest-rectangle-in-histogram/) |

**核心思路：**
- 单调栈用于"下一个更大/更小元素"类问题，模板固定，熟练后秒出
- 84 是单调栈最经典的困难题：维护一个单调递增栈，遇到更矮的柱子时弹栈计算面积，注意哨兵处理边界

---

## 第二阶段 · 滑动窗口 & 二分查找 & 前缀和（2-3 周 · 16 题）

> 掌握三大通用技巧，能解决大量字符串和数组问题。

### 滑动窗口

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 3 | 无重复字符的最长子串 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) |
| 121 | 买卖股票的最佳时机 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) |
| 424 | 替换后的最长重复字符 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-repeating-character-replacement/) |
| 567 | 字符串的排列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/permutation-in-string/) |
| 239 | 滑动窗口最大值 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/sliding-window-maximum/) |
| 76 | 最小覆盖子串 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/minimum-window-substring/) |

**核心思路：**
- 滑动窗口 = 左右指针 + 窗口内状态维护，关键在于**何时收缩左边界**
- 239 滑动窗口最大值：用**单调递减双端队列**维护窗口最大值，队头始终是当前窗口最大值，O(n) 解决

---

### 二分查找

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 704 | 二分查找 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/binary-search/) |
| 35 | 搜索插入位置 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/search-insert-position/) |
| 74 | 搜索二维矩阵 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/search-a-2d-matrix/) |
| 153 | 寻找旋转排序数组中的最小值 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) |
| 33 | 搜索旋转排序数组 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/search-in-rotated-sorted-array/) |

**核心思路：** 二分的本质不是"有序数组查找"，而是**在满足某个条件的边界上二分**，统一写法：`while(l < r)` + 判断 mid 是否满足条件。

---

### 前缀和

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 238 | 除自身以外数组的乘积 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/product-of-array-except-self/) |
| 53 | 最大子数组和 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/maximum-subarray/) |
| 560 | 和为 K 的子数组 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/subarray-sum-equals-k/) |
| 152 | 乘积最大子数组 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/maximum-product-subarray/) |
| 42 | 接雨水 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/trapping-rain-water/) |

**核心思路：** `prefix[i]` = 前 i 个元素之和，区间和 = `prefix[r] - prefix[l-1]`，O(1) 查询任意区间。

---

## 第三阶段 · 树 & 图 & 矩阵（3-4 周 · 28 题）

> 树是面试最高频的数据结构，DFS/BFS 是核心，掌握递归思维。矩阵是图的特殊形式，单独练习。

### 二叉树基础

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 104 | 二叉树的最大深度 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) |
| 226 | 翻转二叉树 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/invert-binary-tree/) |
| 100 | 相同的树 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/same-tree/) |
| 572 | 另一棵树的子树 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/subtree-of-another-tree/) |
| 543 | 二叉树的直径 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/diameter-of-binary-tree/) |
| 110 | 平衡二叉树 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/balanced-binary-tree/) |

**核心思路：** 想清楚两个问题：① 当前节点做什么？② 给父节点返回什么？

---

### BFS 层序遍历

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 102 | 二叉树的层序遍历 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/binary-tree-level-order-traversal/) |
| 199 | 二叉树的右视图 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/binary-tree-right-side-view/) |
| 1448 | 统计二叉树中好节点到根节点路径数 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/) |

---

### BST & 路径

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 98 | 验证二叉搜索树 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/validate-binary-search-tree/) |
| 230 | 二叉搜索树中第 K 小的元素 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) |
| 235 | 二叉搜索树的最近公共祖先 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| 105 | 从前序与中序遍历序列构造二叉树 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 124 | 二叉树中的最大路径和 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) |

---

### 图（DFS / BFS / 拓扑排序）

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 200 | 岛屿数量 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/number-of-islands/) |
| 695 | 岛屿的最大面积 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/max-area-of-island/) |
| 994 | 腐烂的橘子 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/rotting-oranges/) |
| 130 | 被围绕的区域 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/surrounded-regions/) |
| 207 | 课程表（拓扑排序） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/course-schedule/) |
| 417 | 太平洋大西洋水流问题 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/pacific-atlantic-water-flow/) |
| 286 | 墙与门 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/walls-and-gates/) |

---

### 矩阵操作

> ⚠️ 原版路线图缺失此专题，Hot 100 中共有 3～4 道矩阵操作题。

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 73 | 矩阵置零 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/set-matrix-zeroes/) |
| 54 | 螺旋矩阵 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/spiral-matrix/) |
| 48 | 旋转图像 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/rotate-image/) |

**核心思路：**
- 73 矩阵置零：用**第一行/第一列作为标记位**，避免额外空间
- 54 螺旋矩阵：维护 `top/bottom/left/right` 四个边界，按层模拟
- 48 旋转图像：先**沿主对角线转置**，再**水平翻转**，原地完成旋转

---

## 第四阶段 · 动态规划（4-5 周 · 25 题）

> DP 是面试最难、最重要专题。从一维 DP 开始，逐步过渡到二维和背包。

### 一维 DP（入门）

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 70 | 爬楼梯 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/climbing-stairs/) |
| 198 | 打家劫舍 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/house-robber/) |
| 213 | 打家劫舍 II | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/house-robber-ii/) |
| 322 | 零钱兑换 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/coin-change/) |
| 139 | 单词拆分 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/word-break/) |
| 300 | 最长递增子序列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-increasing-subsequence/) |

**做 DP 固定三步：**
1. 定义 `dp[i]` 的含义
2. 写出状态转移方程
3. 确定初始值和遍历顺序

---

### 二维 DP

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 62 | 不同路径 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/unique-paths/) |
| 64 | 最小路径和 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/minimum-path-sum/) |
| 1143 | 最长公共子序列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-common-subsequence/) |
| 72 | 编辑距离 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/edit-distance/) |
| 516 | 最长回文子序列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-palindromic-subsequence/) |
| 312 | 戳气球 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/burst-balloons/) |

---

### 股票系列 & 背包

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 122 | 买卖股票的最佳时机 II | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) |
| 309 | 买卖股票的最佳时机含冷冻期 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| 188 | 买卖股票的最佳时机 IV | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) |
| 416 | 分割等和子集（0-1 背包） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/partition-equal-subset-sum/) |
| 494 | 目标和 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/target-sum/) |

---

### 字符串 DP

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 5 | 最长回文子串 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/longest-palindromic-substring/) |
| 97 | 交错字符串 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/interleaving-string/) |
| 115 | 不同的子序列 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/distinct-subsequences/) |
| 10 | 正则表达式匹配 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/regular-expression-matching/) |

---

## 第五阶段 · 回溯 & 高级数据结构（3-4 周 · 15 题）

> 回溯是枚举型问题的万能框架；堆、Trie、并查集是进阶必备。

### 回溯

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 46 | 全排列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/permutations/) |
| 78 | 子集 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/subsets/) |
| 39 | 组合总和 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/combination-sum/) |
| 131 | 分割回文串 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/palindrome-partitioning/) |
| 79 | 单词搜索 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/word-search/) |
| 51 | N 皇后 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/n-queens/) |

---

### 堆（Heap）

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 215 | 数组中的第 K 个最大元素 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/kth-largest-element-in-an-array/) |
| 347 | 前 K 个高频元素 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/top-k-frequent-elements/) |
| 295 | 数据流的中位数 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/find-median-from-data-stream/) |
| 23 | 合并 K 个升序链表 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/merge-k-sorted-lists/) |

---

### Trie & 并查集

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 208 | 实现 Trie（前缀树） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/implement-trie-prefix-tree/) |
| 212 | 单词搜索 II | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/word-search-ii/) |
| 684 | 冗余连接（并查集） | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/redundant-connection/) |
| 323 | 无向图中连通分量的数目 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/) |
| 4 | 寻找两个正序数组的中位数 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/median-of-two-sorted-arrays/) |

---

## 第六阶段 · 贪心 & 技巧（1-2 周 · 9 题）

> ⚠️ 原版路线图完全缺失本阶段，但 Hot 100 中贪心和技巧类题目合计约 7 道，是送分题的大户。

### 贪心算法

> 贪心的本质：每一步都做**局部最优**选择，推导出全局最优。证明正确性通常靠"交换论证法"。

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 55 | 跳跃游戏 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/jump-game/) |
| 45 | 跳跃游戏 II | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/jump-game-ii/) |
| 763 | 划分字母区间 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/partition-labels/) |

**核心思路：**
- 55/45：维护"当前能跳到的最远位置" `maxReach`，贪心更新，O(n) 完成
- 763：先记录每个字母最后出现位置，再扫描时维护当前区间右边界，到达右边界就切割

---

### 技巧 & 位运算

> 这类题乍看无从下手，但都有固定思路，理解后是纯送分题。

| 题号 | 题目 | 难度 | 链接 |
|:----:|------|:----:|------|
| 136 | 只出现一次的数字 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/single-number/) |
| 169 | 多数元素 | 🟢 简单 | [LeetCode](https://leetcode.cn/problems/majority-element/) |
| 287 | 寻找重复数 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/find-the-duplicate-number/) |
| 41 | 缺失的第一个正数 | 🔴 困难 | [LeetCode](https://leetcode.cn/problems/first-missing-positive/) |
| 31 | 下一个排列 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/next-permutation/) |
| 438 | 找到字符串中所有字母异位词 | 🟡 中等 | [LeetCode](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) |

**核心思路：**
- 136：`a XOR a = 0`，所有数异或一遍，剩下的就是单独的数
- 169：Boyer-Moore 投票算法，维护候选 + 计数，O(n) O(1)
- 287：链表成环思想（同 142），将数组索引当指针，找入环点
- 41：原地哈希，把每个正整数放到对应下标位置，再扫描找第一个空位

---

## 学习方法

### 每道题的做法

1. **独立思考 15 分钟**，实在想不出再看提示
2. **看高票题解**，即使做出来了也要看——最优解往往比你简洁一个量级
3. **隔 3 天默写**，理解后复现是最有效的记忆方式
4. **同类连续做**，一次做完一个专题，而不是零散刷题

### 时间规划参考

| 阶段 | 题数 | 建议时长 |
|------|:----:|:--------:|
| 基础数据结构 | 29 题 | 4–5 周 |
| 滑动窗口 & 二分 & 前缀和 | 16 题 | 2–3 周 |
| 树 & 图 & 矩阵 | 28 题 | 3–4 周 |
| 动态规划 | 25 题 | 4–5 周 |
| 回溯 & 高级结构 | 15 题 | 3–4 周 |
| 贪心 & 技巧 | 9 题 | 1–2 周 |
| **合计** | **122 题** | **17–23 周** |

> 题数略超 100 是因为收录了所有 Hot 100 核心知识点所必须的题目，部分是 Hot 100 的精选延伸题。

### 难度分布

- 🟢 简单：先理解数据结构基本操作，不要跳过
- 🟡 中等：面试主战场，重点攻克
- 🔴 困难：理解思路即可，不强求一次独立写出

### 各专题知识点速查

| 专题 | 核心数据结构 / 算法 |
|------|---------------------|
| 双指针 | left/right 指针、快慢指针 |
| 哈希表 | HashMap、HashSet |
| 链表 | 虚拟头节点、快慢指针、归并 |
| 栈 & 单调栈 | Stack、Deque（单调递增/递减） |
| 滑动窗口 | 双指针 + 哈希/计数器 |
| 二分查找 | `while(l<r)` 统一模板 |
| 前缀和 | prefix 数组 |
| 二叉树 | 递归 DFS、迭代 BFS |
| 图 | visited 数组、队列/栈、邻接表 |
| 矩阵 | 四方向扩展、边界模拟 |
| 动态规划 | dp 定义 + 转移方程 + 初始值 |
| 回溯 | 路径记录 + 撤销 + 剪枝 |
| 堆 | PriorityQueue（大/小顶堆） |
| Trie | TrieNode 数组/哈希 |
| 并查集 | find + union + 路径压缩 |
| 贪心 | 局部最优推全局最优 |
| 位运算 | XOR、二进制技巧 |

---

## 从力扣页面提取原题文案

写笔记里的「原题（力扣中文版）」时，可与站内对照：先用浏览器或 `curl` 保存题目描述页 HTML，再运行仓库中的 [`scripts/extract_lc_cn_meta.py`](scripts/extract_lc_cn_meta.py)，从 `<meta name="description">` 里抽出题干、示例、提示等正文（不含 LaTeX 渲染，可能含站内超链接片段，粘贴后按需删改；提示里的指数在 meta 里有时会被压成普通数字，宜与网页逐字核对）。

```bash
curl.exe -L -o two-sum.html "https://leetcode.cn/problems/two-sum/description/"
python scripts/extract_lc_cn_meta.py two-sum.html -o two-sum-meta.txt
```

## 笔记模板

与现有示例（如 [`001-两数之和.md`](notes/第一阶段-基础数据结构/数组与双指针/001-两数之和.md)）保持一致，每题**单独一个** Markdown 文件，路径见上文 [仓库目录结构](#仓库目录结构)。

### 章节结构一览

| 顺序 | 章节 | 写什么 |
|:----:|------|--------|
| 1 | `# 题号. 题目名称` | 一级标题 |
| 2 | 元信息列表 | 链接、难度、专题、**语言（Python 3）**、完成日期 |
| 3 | `## 题意理解` | 输入输出、约束，用自己的话概括 |
| 4 | `## 思路（多解法）` | `### 思路 A/B/…`，推荐做法可标注 **——推荐**；可加短列表补充细节 |
| 5 | `## 核心代码（Python 3）` | 与思路对应，分 `### A.` `### B.` 小节，每节一个代码块 |
| 6 | `## 复杂度分析` | 多做法时用 **表格**（方法 / 时间 / 空间）；单做法可用列表 |
| 7 | `## 易错点 / 收获` | 边界、循环不变量、可与哪题类比 |

**说明：** 若题目只需一种解法，可将「思路（多解法）」改为「思路」，复杂度用列表即可。若希望笔记中带与力扣一致的原题、示例与提示，可在元信息列表之后增加 `## 原题（力扣中文版）` 小节；摘录时可复用 [`scripts/extract_lc_cn_meta.py`](scripts/extract_lc_cn_meta.py)，用法见 [从力扣页面提取原题文案](#从力扣页面提取原题文案)。

### 可复制骨架

以下整块是一个「模板正文」示例；在 Markdown 里用**四个反引号**包裹整段，这样内部的 Python 仍可用三个反引号正常高亮。

````markdown
# 26. 题目简称

- 链接：https://leetcode.cn/problems/xxx/
- 难度：🟢 简单
- 专题：数组 / 双指针
- **语言：Python 3**（本仓库 Hot 100 笔记与示例代码统一使用 Python）
- 完成日期：YYYY-MM-DD

## 题意理解

用自己的话写：给定什么、求什么、有哪些限制。

## 思路（多解法）

### 思路 A：做法名称 ——推荐

主要步骤一两段话说明；必要时用短列表补充「为什么」「注意什么」。

### 思路 B：另一种做法

……

## 核心代码（Python 3）

### A. 与思路 A 对应的实现

```python
def solution(nums: list[int]) -> int:
    pass
```

### B. 与思路 B 对应的实现（可选）

```python
def solution_alt(nums: list[int]) -> int:
    pass
```

## 复杂度分析

| 方法 | 时间 | 空间 |
|------|------|------|
| 思路 A | O(n) | O(1) |
| 思路 B | O(n²) | O(1) |

## 易错点 / 收获

- 边界：...
- 与 **题号 题目名** 的共同点 / 区别：...
````

---

*最后更新：2026-04*