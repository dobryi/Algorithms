import random
from sorting import insertion_sort
from searching import find_max, find_min


def solomon_sort(seq):
    n, min_a, max_a = len(seq), find_min.find_min(seq), find_max.find_max(seq)
    delta = (max_a - min_a) / n
    buckets = [[] for _ in range(n)]
    print(delta)
    for i in range(n):
        new_index = (seq[i] - min_a) / delta if (seq[i] - min_a) / delta > 1 else 1
        buckets[int(new_index) - 1].append(seq[i])
    j = 0
    for bucket_i in range(n):
        if buckets[bucket_i]:
            buckets[bucket_i] = insertion_sort.insertion_sort(buckets[bucket_i])
            for i in range(len(buckets[bucket_i])):
                seq[j] = buckets[bucket_i][i]
                j += 1
    return seq

if __name__ == '__main__':
    test_seq = [random.randint(-20, 20) for _ in range(20)]
    print(test_seq)
    sorted_test_seq = solomon_sort(test_seq.copy())
    print(sorted_test_seq)
    assert sorted_test_seq == sorted(test_seq)
