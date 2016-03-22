import random


def find_min_w_limits(seq, low, high):
    min_a, n = None, len(seq)
    for i in range(n):
        if seq[i] >= low:
            if high >= seq[i]:
                if min_a is None or min_a > seq[i]:
                    min_a = seq[i]
    return min_a

test_seq = [random.randint(-20, 20) for _ in range(20)]
lo, hi = random.randint(6, 10), random.randint(12, 16)
print(test_seq, lo, hi)
print(find_min_w_limits(test_seq, lo, hi))
