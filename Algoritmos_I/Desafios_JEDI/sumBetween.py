def sumBetween(numbers, ranges):
    sums = []
    for item in ranges:
        sums.append(sum(numbers[item[0]:item[1] + 1]))
    return max(sums)



A = [1, -2, 3, 4, -5, -4, 3, 2, 1]
ranges = [(1, 3), (0, 4), (6, 8)]

print(sumBetween(A, ranges))
