import random


def quick_sort(seq):
    left, right, middle, n = [], [], [], len(seq)
    if n < 2:
        return seq
    pivot = seq[0]
    for i in range(n):
        if seq[i] < pivot:
            left.append(seq[i])
        elif seq[i] > pivot:
            right.append(seq[i])
        else:
            middle.append(seq[i])
    return quick_sort(left) + middle + quick_sort(right)

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = quick_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
