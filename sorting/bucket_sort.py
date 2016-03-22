import random
from math import ceil
from sorting import insertion_sort
from searching import find_min, find_max


def bucket_sort(seq, num_of_buckets=10):
    n = len(seq)
    min_a = find_min.find_min(seq)
    for i in range(n):
        seq[i] += abs(min_a)
    buckets = [[] for _ in range(num_of_buckets)]
    max_a = find_max.find_max(seq)
    divider = ceil((max_a + 1) / num_of_buckets)
    for i in range(n):
        buckets[int(seq[i] // divider)].append(seq[i])
    j = 0
    for bucket_i in range(num_of_buckets):
        if buckets[bucket_i]:
            buckets[bucket_i] = insertion_sort.insertion_sort(buckets[bucket_i])
            for k in range(len(buckets[bucket_i])):
                seq[j] = buckets[bucket_i][k]
                j += 1
    for i in range(n):
        seq[i] += min_a
    return seq

if __name__ == '__main__':
    test_seq = [random.randint(-20, 20) for _ in range(20)]
    print(test_seq)
    sorted_test_seq = bucket_sort(test_seq.copy(), 12)
    print(sorted_test_seq)
    assert sorted_test_seq == sorted(test_seq)
