
# tail redursion:
def tail(n):
    if n==0:
        return
    print(n)

    tail(n-1)

# head recursion
def head(n):
    if n == 0:
        return
    head(n-1)
    print(n)

if __name__ == "__main__":
    head(5)