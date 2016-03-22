import random


def shell_sort(seq):
    sedgewick, n = [], len(seq)
    for i in range(n):
        if i % 2 == 0:
            sedgewick.append(9 * pow(2, i) - 9 * pow(2, i // 2) + 1)
        else:
            sedgewick.append(8 * pow(2, i) - 6 * pow(2, (i + 1) // 2) + 1)
        if 3 * sedgewick[-1] > n:
            break
    # print(sedgewick)
    for step in reversed(sedgewick):
        block = seq[::step]
        insertion_sort(block)
        seq[::step] = block
    return seq


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        min_a, j = seq[i], i - 1
        while seq[j] > min_a and j > -1:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = min_a
    return seq

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = shell_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
