import threading
from concurrent.futures.thread import ThreadPoolExecutor
from random import randint
from time import sleep


class Account:
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.RLock() # 互斥锁，允许同一线程多次请求
        self.condition = threading.Condition(lock) # 创建条件变量，用于线程间通知/等待机制

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()  # 账户余额不足，则等待
            sleep(0.001)
            self.balance -= money

    def deposit(self, money):
        """存钱"""
        with self.condition:
            sleep(0.001)
            self.balance += money
            self.condition.notify_all()

    def add_money(self):
        """模拟存钱"""
        money = randint(5, 10)
        self.deposit(money)
        print(threading.current_thread().name, "存:", money, "===> 当前余额：", self.balance)
        sleep(0.5)

    def sub_money(self):
        """模拟取钱"""
        money = randint(10, 30)
        self.withdraw(money)
        print(threading.current_thread().name, "取:", money, "===> 当前余额：", self.balance)
        sleep(0.5)

if __name__ == '__main__':
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):  # 存钱模拟5次
            pool.submit(account.add_money)
        for _ in range(10):
            pool.submit(account.sub_money)
