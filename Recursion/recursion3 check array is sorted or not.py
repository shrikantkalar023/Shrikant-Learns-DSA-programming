#Checking if array is sorted or not using recursion

def arst(ar,i=0):
    if i==len(ar)-1: #base case
        return True
    else:
        return ar[i]<=ar[i+1] and arst(ar,i+1) #small problem call & calc both
        
