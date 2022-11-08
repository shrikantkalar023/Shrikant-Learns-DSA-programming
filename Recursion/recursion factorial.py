#factorial using recursion

def fac(n):
    if n==1 or n==0: #base
        return 1
    else:
        return n*fac(n-1) #small problem
