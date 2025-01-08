def prime(k):
    initial = 2
    if k == 1:
        return "not prime"
    while initial < k:
        if k % initial == 0:
            return "not prime"
        else:
            initial = initial + 1
    return "is prime"