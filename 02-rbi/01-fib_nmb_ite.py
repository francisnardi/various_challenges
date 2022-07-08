def fib_nmb_ite(n):

    a = 0
    b = 1
    if (n < 1):
        return
    print(a, end=" ")
    for i in range(1, n):
        print(b, end=" ")
        nxt = a + b
        a = b
        b = nxt


def fib_nmb_rec(nmb):
    if nmb == 0:
        return 0
    elif nmb == 1:
        return 1
    else:
        return fib_nmb_rec(nmb-2)+fib_nmb_rec(nmb-1)


def print_fib_nmb_rec(n):
    for i in range(0, n):
        print(fib_nmb_rec(i), end=" ")


if __name__ == '__main__':
    # Recursive
    # print_fib_nmb_rec(100)

    # Iterative
    fib_nmb_ite(100)
