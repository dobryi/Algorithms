import random
from sorting import insertion_sort
from searching import find_min


def flash_sort(seq):
    n, min_a = len(seq), find_min.find_min(seq)
    max_i = 0
    for i in range(n):
        if seq[max_i] < seq[i]:
            max_i = i
    m = int(0.42 * n)
    cft = (m - 1) / (seq[max_i] - min_a)
    dist_table = [0 for _ in range(m)]
    for i in range(n):
        dist_table[int(cft * (seq[i] - min_a))] += 1
    print(dist_table)
    for k in range(1, m):
        dist_table[k] += dist_table[k - 1]
    print(dist_table)
    seq[0], seq[max_i] = seq[max_i], seq[0]
    moves, j = 0, 0
    k = m - 1
    print(seq)
    while moves < n - 1:
        while j > (dist_table[k] - 1):
            j += 1
            k = int(cft * (seq[j] - min_a))
            print(j)
        while j != dist_table[k]:
            k = int(cft * (seq[j] - min_a))
            seq[dist_table[k] - 1], seq[j] = seq[j], seq[dist_table[k] - 1]
            dist_table[k] -= 1
            moves += 1
            print(seq, dist_table)
    return insertion_sort.insertion_sort(seq)

if __name__ == '__main__':
    test_seq = [random.randint(-11, 11) for _ in range(11)]
    print(test_seq)
    sorted_test_seq = flash_sort(test_seq.copy())
    print(sorted_test_seq)
    assert sorted_test_seq == sorted(test_seq)
