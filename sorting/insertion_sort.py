import random


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        min_a, j = seq[i], i - 1
        while seq[j] > min_a and j > -1:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = min_a
    return seq

if __name__ == '__main__':
    test_seq = [random.randint(-20, 20) for _ in range(20)]
    print(test_seq)
    sorted_test_seq = insertion_sort(test_seq.copy())
    print(sorted_test_seq)
    assert sorted_test_seq == sorted(test_seq)
