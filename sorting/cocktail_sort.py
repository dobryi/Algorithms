import random


def cocktail_sort(seq):
    swapped, start, end, inverted = True, 0, len(seq) - 1, False
    while swapped:
        swapped = False
        for i in sorted(range(start, end), reverse=inverted):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if inverted:
            start += 1
        else:
            end -= 1
        inverted = not inverted
    return seq

test_seq = [random.randint(-20, 20) for _ in range(20)]
print(test_seq)
sorted_test_seq = cocktail_sort(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
