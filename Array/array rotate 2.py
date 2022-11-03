#array rotation
#rotating by one element to get the desired rotation of r steps

def rotatearray(a1,r,di):
    l=len(a1) #elements in a1 array

    for j in range(0,r):
        if di==1:
            #print('di1-left')
            le=a1[0]
            for i in range(0,l-1):
                #print(i,i+1)
                a1[i]=a1[i+1]
                #print(a1)
            a1[l-1]=le
        else:
            #print('di2-right')
            le=a1[l-1]
            for i in range(l-2,-1,-1):
                #print(i+1,i)
                a1[i+1]=a1[i]
                #print(a1)
            a1[0]=le
    return(a1)
            
            
            
        
