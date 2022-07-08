# Write a code which finds the NEXT higher number using the same given digits of a given integer. i.e.,
# if the given integer is 1234, you should return 1243.

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
    value1 = "1234"
    #output1: "1243"
    value2 = "218765"
    # output2 = "251678"
    value3 = "4321"
    #output3: "Impossible to find a NEXT higher number"
    value4 = "534976"
    #output4: "536479"

    find_next(value1, len(value1))
    find_next(value2, len(value2))
    find_next(value3, len(value3))
    find_next(value4, len(value4))