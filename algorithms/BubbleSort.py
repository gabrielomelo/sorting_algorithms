"""
    Implementação batuta do Bubble Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time


class BubbleSort(SortAlgorithm):

    def __init__(self, array, timeout):
        self.arr = array
        self.timeout = (timeout/1000) * 2

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr) - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                time.sleep(self.timeout)
