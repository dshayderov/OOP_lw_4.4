#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая будет генерировать матрицу из случайных целых чисел.
Пользователь может указать число строк и столбцов, а также диапазон целых чисел.
Произведите обработку ошибок ввода пользователя.
"""

import random


class Matrix:

    def __init__(self, rows, cols, start, end):
        self.rows = int(rows)
        self.cols = int(cols)
        self.start = int(start)
        self.end = int(end)

        self.matrix = [[random.randint(self.start, self.end) for j
                        in enumerate([1] * self.cols)] for i
                       in enumerate([1] * self.rows)]

    def __str__(self):
        s = ""
        for row in self.matrix:
            s += str(row) + "\n"

        return s


if __name__ == "__main__":
    try:
        n = input("Количество строк матрицы: ")
        k = input("Количество столбцов матрицы: ")
        x = input("Начало диапазона чисел: ")
        y = input("Конец диапазона чисел: ")

        if int(x) > int(y) or int(n) <= 0 or int(k) <= 0:
            raise Exception("Неверно введены параметры матрицы")

    except Exception as e:
        print(str(e))
        exit(1)

    print(Matrix(n, k, x, y))