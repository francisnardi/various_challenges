# Write a function that, given a vector and a target sum, returns zero-based indices of any two distinct elements whose sum is equal to the target sum. 
# If there are no such elements, the function should return (-1, -1).
# For example, findTwoSum({ 1, 3, 5, 7, 9 }, 12) should return any of the following pairs of indices:

# 1, 4 (3 + 9 = 12)
# 2, 3 (5 + 7 = 12)
# 3, 2 (7 + 5 = 12)
# 4, 1 (9 + 3 = 12)

def find_two_sum(arr, n):
    idxs = {}
    for ind, number in enumerate(arr):
        idxs.setdefault(number, []).append(ind)
    for j, k in idxs.items():
        elem = k.pop()
        dif = n - j
        if dif in idxs and idxs[n-j]:
            return elem, idxs[n-j].pop()


def print_fts(arr, n):
    result = find_two_sum(arr, n)
    print(result) if result else print((-1, -1))


if __name__ == '__main__':
    print_fts([1, 3, 5, 7, 9], 12)