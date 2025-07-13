
def prime(n):
    result = list()
    while n >= 2:
        go_prime = True
        for i in range(2, n + 1):
            if n % i == 0 and n != i:
                go_prime = False
                break
        if go_prime:
            result.append(n)
        n = n - 1
    print(result)


prime(100)
