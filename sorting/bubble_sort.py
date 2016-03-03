import random


def bubble_sort(seq):
    swapped, n = True, len(seq)
    while swapped:
        swapped = False
        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        n -= 1
    return seq

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = bubble_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
