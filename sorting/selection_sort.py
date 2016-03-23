import random


def selection_sort(seq):
    n = len(seq)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_i]:
                min_i = j
        if min_i != i:
            seq[min_i], seq[i] = seq[i], seq[min_i]
    return seq

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = selection_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
