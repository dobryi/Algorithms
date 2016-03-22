import random


def find_min(seq):
    min_a, n = seq[0], len(seq)
    for i in range(n):
        if min_a > seq[i]:
            min_a = seq[i]
    return min_a

if __name__ == '__main__':
    test_seq = [random.randint(-10, 10) for _ in range(10)]
    print(test_seq)
    print(find_min(test_seq))