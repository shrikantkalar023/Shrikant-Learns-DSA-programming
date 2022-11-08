#fibonacci series using recursion

def fib(n):
    if n==1 or n==0: #base
        return 1
    else:
        return fib(n-1)+fib(n-2) #small problem


for i in range(0,15):
    print(fib(i),end=' ')
