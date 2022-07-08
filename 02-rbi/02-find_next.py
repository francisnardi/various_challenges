def find_next(value, n):

    number = list(map(int, value))

    for i in range(n-1, 0, -1):
        if number[i] > number[i-1]:
            break

    if i == 1 and number[i] <= number[i-1]:
        print("Impossible to find a NEXT higher number")
        return

    nxt = number[i-1]
    smll = i
    for j in range(i+1, n):
        if number[j] > nxt and number[j] < number[smll]:
            smll = j

    number[smll], number[i-1] = number[i-1], number[smll]

    nxt = 0
    for j in range(i):
        nxt = nxt * 10 + number[j]

    number = sorted(number[i:])
    for j in range(n-i):
        nxt = nxt * 10 + number[j]

    print("NEXT higher number is", nxt)


if __name__ == '__main__':
    value = "1234"
    find_next(value, len(value))