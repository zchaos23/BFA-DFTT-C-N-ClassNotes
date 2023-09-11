"""
提交如下程序:
◎动态规划法:0-1背包问题(后附伪代码)，回答以这个 程序为基础能够实现穷举法吗?(要求:输出结果包含必 要有价值的信息，从算法层面注释清楚)
◎回溯法:N皇后问题(要求:输出结果包含必要有价值的 信息，从算法层面注释清楚)
◎选做:实现回溯法N皇后问题或四色问题的可视化程序 (选做提交时间可延长)
"""


maxW = 100
V = [10, 40, 30, 50, 35, 40, 30]
W = [35, 30, 60, 50, 40, 10, 25]


def bag01(i, maxW, V, W):
    # 当没有物品可选或背包重量为零时，返回 0
    if i == 0 or maxW == 0:
        return 0
    # 如果当前物品重量大于背包重量，则无法装入
    if W[i-1] > maxW:
        return bag01(i-1, maxW, V, W)
    # 如果非以上两种情况，返回装或不装当前物品时的最大价值
    return max(V[i-1]+bag01(i-1, maxW-W[i-1], V, W), bag01(i-1, maxW, V, W))


print("背包能容纳的最大价值：", bag01(len(V), maxW, V, W))


# n 为棋盘行列数，m 为防止超出列表元素个数的偏移量， queen 为皇后放置的行列坐标
n = 8
m = n - 1
queen = {}

# a, b, c 分别为列、右上对角线，右下对角线不可放置皇后的列表
a = []
b = []
c = []

# 生成列表
for i in range(m + n):
    if i < n:
        a.append(0)
    b.append(0)
    c.append(0)

# 计数
count = 0


# N皇后问题程序
def n_queens(i):
    global count
    # 尝试 i 行的每个列
    for j in range(n):
        # 判断可否放置
        if a[j] == 0 and b[i-j+m] == 0 and c[i+j] == 0:
            # 放置皇后，并写入列、右上对角线，右下对角线不可放置皇后的列表
            queen[(i, j)] = 'Q'
            a[j] = 1
            b[i-j+m] = 1
            c[i+j] = 1
            # 未完全解出，回溯继续尝试
            if i < m:
                n_queens(i+1)
            # 完成一次解，计数
            else:
                count += 1

            queen[(i, j)] = '*'
            a[j] = 0
            b[i - j + m] = 0
            c[i + j] = 0

    return count


print("{}皇后问题的解有{}种".format(n, n_queens(0)))
