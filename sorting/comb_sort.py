import random

FACTOR = 1.247330950103979


def comb_sort(seq):
    swapped, n = True, len(seq)
    step = int(n // FACTOR)
    while step > 1:
        for i in range(n - step):
            if seq[i] > seq[i + step]:
                seq[i], seq[i + step] = seq[i + step], seq[i]
        step = int(step // FACTOR) or 1
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
sorted_test_seq = comb_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)

