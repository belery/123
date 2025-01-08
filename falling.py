def falling(n, k):
    total = 1
    while k == 0:
        return 1

    while n > k:
        total, n = total * n, n - 1
    return total
