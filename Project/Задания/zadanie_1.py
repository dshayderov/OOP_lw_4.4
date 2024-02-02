#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
 т. е. соединение, строк. В остальных случаях введенные числа суммируются.
"""


class SumConc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

        if isinstance(self.a, int) and isinstance(self.b, int):
            self.res = int(self.a) + int(self.b)
        else:
            self.res = str(a + b)

    def __str__(self):
        return f"Результат: {self.res}"


if __name__ == "__main__":
    x = input("Первое значение: ")
    y = input("Второе значение: ")

    print(SumConc(x, y))