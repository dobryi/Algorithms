import random


def merge_sort(seq):
    n = len(seq)
    if n == 1:
        return seq
    left, right, li, ri, i = merge_sort(seq[:n // 2]), merge_sort(seq[n // 2:]), 0, 0, 0
    print(left, right)
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            seq[i] = left[li]
            li += 1
        elif right[ri] < left[li]:
            seq[i] = right[ri]
            ri += 1
        else:
            seq[i] = left[li]
            i += 1
            seq[i] = right[ri]
            li += 1
            ri += 1
        i += 1
    seq[i:] = right[ri:] or left[li:]
    return seq

test_seq = [random.randint(-5, 5) for _ in range(9)]
print(test_seq)
sorted_test_seq = merge_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
