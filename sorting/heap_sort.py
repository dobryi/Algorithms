import random
from math import log2


def heap_sort(seq):

    def heapify(idx, length):
        largest = idx
        left_child = (idx << 1) + 1
        right_child = (idx << 1) + 2
        if left_child < length:
            largest = left_child if seq[left_child] > seq[largest] else largest
        if right_child < length:
            largest = right_child if seq[right_child] > seq[largest] else largest
        if idx != largest:
            seq[largest], seq[idx] = seq[idx], seq[largest]
            heapify(largest, length)
    n = len(seq)
    for i in range(n // 2, -1, -1):
        heapify(i, n)
    print(seq)
    for j in [pow(2, x) for x in range(int(log2(n)) + 1)]:
        print(" " * (n - j), seq[j - 1: 2 * j - 1])
    for k in range(n - 1, -1, -1):
        seq[0], seq[k] = seq[k], seq[0]
        heapify(0, k)
    return seq


test_seq = [random.randint(0, 20) for _ in range(9)]
print(test_seq)
sorted_test_seq = heap_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
