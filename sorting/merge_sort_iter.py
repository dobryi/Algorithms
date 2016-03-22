import random


def merge_sort_iter(seq):
    block_size, n = 2, len(seq)
    while block_size <= 2 * n:
        for bi in range(n // block_size + 1):
            block = seq[bi * block_size: block_size * (bi + 1)]
            if block:
                print(block_size, block)
                split_and_merge_block(block, block_size)
                seq[bi * block_size: block_size * (bi + 1)] = block
        block_size *= 2
    return seq


def split_and_merge_block(block, block_size):
    left, right = block[:block_size // 2], block[block_size // 2:]
    li, ri, i = 0, 0, 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            block[i] = left[li]
            li += 1
        elif right[ri] < left[li]:
            block[i] = right[ri]
            ri += 1
        else:
            block[i] = left[li]
            i += 1
            block[i] = right[ri]
            li += 1
            ri += 1
        i += 1
    block[i:] = right[ri:] or left[li:]


test_seq = [random.randint(-10, 10) for _ in range(15)]
print(test_seq)
sorted_test_seq = merge_sort_iter(test_seq.copy())
print(sorted_test_seq)
assert sorted_test_seq == sorted(test_seq)
