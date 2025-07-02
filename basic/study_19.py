import glob
import os.path
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

PREFIX = "thumbnails"


def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)


def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            # 创建开启线程
            threading.Thread(
                target=generate_thumbnail,
                args=(infile, (size, size))
            ).start()


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        """存款方法"""
        # 通过锁来保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


def account_test():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    # 将多线程任务加入列表
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 执行
    for future in futures:
        future.result()
    # 关闭线程池
    pool.shutdown()

    print(account.balance)


if __name__ == '__main__':
    main()
    account_test()
