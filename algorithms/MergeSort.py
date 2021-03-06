"""
    Implementação batuta do Merge Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm as Parent
from math import floor
import time


class MergeSort(Parent):

    def __init__(self, dataset, timeout):
        self.arr = dataset
        self.size = len(self.arr)
        self.timeout = (timeout/1000) * 2

    def sort(self):
        self.merge_sort(self.arr, 0, len(self.arr) - 1)

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i, j, k = (0,0,l)

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr, l, r):
        if l < r:
            m = floor((l+r)/2)
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)
        time.sleep(self.timeout)