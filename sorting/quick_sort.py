import random


def quick_sort(seq):
    n = len(seq)
    pivot, left, right = seq[int(n // 2)], 0, n - 1
    while left <= right:
        print(pivot, left, right)
        while seq[left] < pivot and left < n:
            left += 1
        while seq[right] > pivot and right > -1:
            right -= 1
        if left <= right:
            seq[left], seq[right] = seq[right], seq[left]

    return seq

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = quick_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
