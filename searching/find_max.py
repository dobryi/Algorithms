import random


def find_max(seq):
    max_a, n = seq[0], len(seq)
    for i in range(n):
        if max_a < seq[i]:
            max_a = seq[i]
    return max_a

if __name__ == '__main__':
    test_seq = [random.randint(-10, 10) for _ in range(10)]
    print(test_seq)
    print(find_max(test_seq))