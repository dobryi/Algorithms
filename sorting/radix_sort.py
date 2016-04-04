import random
from sorting import insertion_sort
from searching import find_min, find_max


def radix_sort(seq):
    n, divisor = len(seq), 10
    min_a, max_a = find_min.find_min(seq), find_max.find_max(seq)
    for i in range(n):
        seq[i] += abs(min_a)
    while divisor / 10 <= max_a:
        blocks = [[] for _ in range(10)]
        for i in range(n):
            digit = seq[i] % divisor - seq[i] % (int(divisor / 10))
            while digit >= 10:
                digit /= 10
            print(seq[i], digit, divisor)
            blocks[int(digit)].append(seq[i])
        j = 0
        for block_i in range(10):
            if blocks[block_i]:
                blocks[block_i] = insertion_sort.insertion_sort(blocks[block_i])
                for k in range(len(blocks[block_i])):
                    seq[j] = blocks[block_i][k]
                    j += 1
        divisor *= 10
    for i in range(n):
        seq[i] += min_a
    return seq

if __name__ == '__main__':
    test_seq = [random.randint(-20, 20) for _ in range(20)]
    print(test_seq)
    sorted_test_seq = radix_sort(test_seq.copy())
    print(sorted_test_seq)
    assert sorted_test_seq == sorted(test_seq)
