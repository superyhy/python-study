class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())  # 背包最大承重和物品数量
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))  # 物品信息
    all_things.sort(key=lambda x: x.value, reverse=True)  # 物品按照价值排序
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值：{total_price}美元')


def _partition(items, start, end, comp):
    """分区函数，选定基准值，保证左边小于基准值，右边大于基准值"""
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def _quick_sort(items, start, end, comp):
    """左右两侧 递归调用"""
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]  # 创建副本
    _quick_sort(items, 0, len(items) - 1, comp);
    return items


if __name__ == '__main__':
    # 调用快速排序
    list1 = [12, 4, 12, 45, 3, 2, 123, 1]
    print(quick_sort(list1))
    # map对象为惰性迭代器，将一个函数应用到一个可迭代对象上面，再使用list进行类型转换
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
