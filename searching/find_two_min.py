import random


def find_two_min(seq):
    min1, min2, n = seq[0], seq[0], len(seq)
    for i in range(n):
        if min1 > seq[i]:
            min2 = min1
            min1 = seq[i]
        elif min2 > seq[i]:
            min2 = seq[i]
    return min1, min2

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
print(find_two_min(test_seq))
