#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread

"""
Условие задачи:
    * потребитель: клиент, обратившийся в тех. поддержку
    * производитель: оператор, принимающий звонки клиентов
"""


def consumer():
    lock.acquire()
    ls = []
    while not q.empty():
        s = q.get()
        r = random.choice(["Необходима помощь", "Частично решена", "Решена"])
        print(f"Клиент с id: {s[1]} столкнулся с проблемой: {s[0]}, Результат: {r}")
        ls.append(
            {
                "id": s[1],
                "Проблема": s[0],
                "Результат": r
            }
        )
    for i in ls:
        if i["Результат"] == "Необходима помощь":
            print(f"Клиент с id {i['id']} ожидает мастера")
    lock.release()


def producer(ls):
    lock.acquire()
    ls = ls
    for i in range(6):
        idx = random.randint(0, 3)
        exp = random.randint(1, 1000)
        q.put([ls[idx], exp])
    lock.release()


if __name__ == "__main__":
    ls = ['Бесконечная загрузка', 'Не проходит оплата', 'Проблема со связью', 'Нет расписания']
    lock = Lock()
    q = Queue()
    q2 = Queue()
    th1 = Thread(target=producer(ls)).start()
    th2 = Thread(target=consumer()).start()
