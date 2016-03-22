import random


def find_two_max(seq):
    max1, max2, n = seq[0], seq[0], len(seq)
    for i in range(n):
        if max1 < seq[i]:
            max2 = max1
            max1 = seq[i]
        elif max2 < seq[i]:
            max2 = seq[i]
    return max1, max2

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
print(find_two_max(test_seq))
