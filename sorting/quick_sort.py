import random


def quick_sort(seq):
    n = len(seq)
    if n == 1:
        return seq
    pivot, pivot_i = seq[0], 0
    for i in range(1, n):
        if seq[i] < pivot:
            seq[pivot_i], seq[i] = seq[i], seq[pivot_i]
            pivot_i = i


    return seq


#test_seq = [random.randint(-20, 20) for _ in range(20)]
test_seq = [9, 6, 3, 4, 10, 8, 2, 7]
print(test_seq)
sorted_test_seq = quick_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
