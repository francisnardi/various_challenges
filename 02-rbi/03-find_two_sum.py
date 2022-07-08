def find_two_sum(arr, n):
    idxs = {}
    for ind, number in enumerate(arr):
        idxs.setdefault(number, []).append(ind)
    for j, k in idxs.items():
        i = k.pop()
        if n - j in idxs and idxs[n-j]:
            return i, idxs[n-j].pop()


def print_fts(arr, n):
    result = find_two_sum(arr, n)
    print(result) if result else print((-1, -1))


if __name__ == '__main__':
    print_fts([1, 3, 5, 7, 9], 12)