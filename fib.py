def fib(n):
        f = [None] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
                f[i] = f[i-1] + f[i-2]
        print f[n-1]
