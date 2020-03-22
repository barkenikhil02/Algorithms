def fact(n):
    if n==1:
        return 1
    # subRes1 = fact(n-1)
    # subRes2 = n*subRes1
    # return n*fact(n-1)
    return n*fact(n-1)

def fact_acc(n,acc=1):
    if n==1:
        return acc
    return fact_acc(n-1,n*acc)

if __name__ == "__main__":
    print(fact_acc(5))