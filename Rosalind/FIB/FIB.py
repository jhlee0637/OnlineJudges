def fib(n,k):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fib(n-1,k)+fib(n-2,k)*k

if __name__=="__main__":
    n=5
    k=3
    #n=
    #k=
    print(fib(n-1,k))

    