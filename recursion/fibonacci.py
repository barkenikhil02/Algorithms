def fibo(n):
    if n==0: return 0
    if n==1: return 1

    fib1 = fibo(n-1)
    fib2 = fibo(n-2)

    return fib1+fib2

if __name__ == "__main__":
    print(fibo(10))