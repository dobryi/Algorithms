import random


def find_both_min_max(seq):
    min_a, max_a, n = seq[0], seq[0], len(seq)
    for i in range(n):
        if min_a > seq[i]:
            min_a = seq[i]
        else:
            if max_a < seq[i]:
                max_a = seq[i]
    return min_a, max_a

test_seq = [random.randint(-10, 10) for _ in range(10)]
print(test_seq)
print(find_both_min_max(test_seq))