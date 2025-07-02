def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]  # 创建副本
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]  # 较小值和较大值交换
    return items


def bubble_sort(items, comp=lambda x, y: x > y):  # 方法参数传入比较函数
    """冒泡排序"""
    items = items[:]  # 创建副本，避免对原数据修改
    for i in range(len(items) - 1):
        swapper = False  # 定义交换标识 如果一次循环中没有进行一次交换 则原列表有序
        for j in range(len(items) - i - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapper = True
        if not swapper:
            break
    return items


def bubble_sort_v2(items, comp=lambda x, y: x > y):
    """搅拌排序（冒泡排序升级版）,正向和反向冒泡结合，减少时间复杂度"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
            if swapped:
                swapped = False
                for j in range(len(items) - 2 - i, i, -1):
                    if comp(items[j - 1], items[j]):
                        items[j], items[j - 1] = items[j - 1], items[j]
                        swapped = True
            if not swapped:
                break
    return items


def merge(items1, items2, comp=lambda x, y: x < y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    """执行归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1




if __name__ == '__main__':
    list = [12, 3, 34, 6, 56, 7, 26, 10, 13, 37]
    print(select_sort(list))
    list2 = [12, 3, 34, 6, 56, 7, 26, 10, 13, 37]
    print(bubble_sort(list2))
    list3 = [12, 3, 34, 6, 56, 7, 26, 10, 13, 37]
    print(bubble_sort_v2(list3))
    list4 = [12, 3, 34, 6, 56, 7, 26, 10, 13, 37]
    print(bin_search(list4, 56))
    print(merge_sort(list4))
