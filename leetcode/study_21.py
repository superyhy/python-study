import asyncio


def num_generator(m, n):
    """指定范围的数字生成去"""
    yield from range(m, n + 1)  # 生成指定范围的数字序列


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):  # 判断数字i是否为素数
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime==>', i)
            primes.append(i)

        await asyncio.sleep(0.001)  # 在异步函数中暂停当前协程（任务）0.001秒
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射桥"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 获取当前线程的事件循环对象
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))  # 将两个协程任务，打包成一个任务组
    future.add_done_callback(lambda x: print(x.result()))  # 执行所有任务，全部完成后返回结果列表
    loop.run_until_complete(future)  # 运行直到future执行完成为止
    loop.close()  # 释放资源
