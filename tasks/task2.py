#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from threading import Lock, Thread
from queue import Queue

EPS = 1e-07


def func2():
    while True:
        s = q.get()
        y = 1/s
        print(f'y = {y}')
        if q.empty():
            break


def func1():
    lock.acquire()
    x = 0.3
    S, n = 0, 1
    while True:
        S1 = math.pow(x, n)
        n += 1
        S2 = math.pow(x, n)
        if abs(S2 - S1) < EPS:
            break
        S += S2
        print(f"S = {S}")
        q.put(S)

    lock.release()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    th1 = Thread(target=func1).start()
    th2 = Thread(target=func2).start()