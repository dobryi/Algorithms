import random


def effective_find_max(seq):
    n = len(seq)
    for i in range(0, n - 1, 2):
        if seq[i + 1] < seq[i]:
            seq[i + 1], seq[i] = seq[i], seq[i + 1]
    min_a, max_a = seq[-1], seq[-1]
    for i in range(0, n - 1, 2):
        if seq[i] < min_a:
            min_a = seq[i]
        if seq[i + 1] > max_a:
            max_a = seq[i + 1]
    return min_a, max_a

test_seq = [random.randint(-20, 20) for _ in range(19)]
print(test_seq)
print(effective_find_max(test_seq))
