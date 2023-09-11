"""
提交如下程序:

递归二分检索(要求:显示检索结果，每次检索中间值，检索次数)
冒泡排序(要求:注释解释清楚算法，显示每一步中间结果)
"""

data = [3, 5, 58, 62, 116, 145, 420, 434, 446, 468,
        473, 516, 539, 585, 607, 608, 718, 813, 870, 916]
item = 5
count = 0


def binary_search(first, last, data, item):
    middle = (first + last) // 2
    global count
    count += 1
    print('第{}次检索, 中间值:{}'.format(count, data[middle]))

    if first > last:
        print('检索完成, 未检索到 {}'.format(item))
        return False
    else:
        if item == data[middle]:
            print('检索完成, 检索到 {}'.format(item))
            return True
        else:
            if item < data[middle]:
                binary_search(first, middle-1, data, item)
            else:
                binary_search(middle+1, last, data, item)


binary_search(0, len(data), data, item)


data = [2, 7, 10, 4, 1, 5, 9, 8, 6, 3]


def bubble_sort():
    # 创建变量，储存列表中首个未完成排序元素的位数
    firstUnsorted = 0
    # 创建变量，用于检测当前 Bubble Up 是否完成
    swap = True
    # 创建变量，统计轮数
    count = 0

    # 当首个未完成排序元素的位数小于列表元素个数且当前 Bubble Up 完成时，进行下一轮 Bubble Up
    while firstUnsorted < len(data)-1 and swap:
        # 赋值当前 Bubble Up 状态为未完成
        swap = False
        # 创建变量，用于比较该列表元素与上一位列表元素
        index = len(data)-1
        # 当该元素位数小于首个未完成排序元素的位数时，说明未完成本次 Bubble Up
        while index > firstUnsorted:
            # 比较该元素与上一位元素，小于时交换位置
            if data[index] < data[index-1]:
                data[index], data[index - 1] = data[index - 1], data[index]
                # 赋值当前 Bubble Up 状态为完成
                swap = True
                # 轮数 + 1
                count += 1
                # 输出本步中间结果
                print("完成第{}步排序，排序中间结果:{}".format(count, data))
            # 继续比较
            index -= 1
        # 完成一轮 Bubble Up 后，将未完成排序元素的位数加一
        firstUnsorted += 1
    # 返回排序完结果
    return data


result = bubble_sort()
print("完成冒泡排序，排序结果: {}".format(result))
