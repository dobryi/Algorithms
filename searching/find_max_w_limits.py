import random


def find_max_w_limits(seq, low, high):
    max_a, n = None, len(seq)
    for i in range(n):
        if seq[i] >= low:
            if high >= seq[i]:
                if max_a is None or max_a < seq[i]:
                    max_a = seq[i]
    return max_a

test_seq = [random.randint(-20, 20) for _ in range(20)]
lo, hi = random.randint(6, 10), random.randint(12, 16)
print(test_seq, lo, hi)
print(find_max_w_limits(test_seq, lo, hi))
