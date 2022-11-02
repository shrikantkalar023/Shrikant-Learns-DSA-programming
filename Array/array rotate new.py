#rotatearay fn take an array and no. of steps of rotation as input. Also it asks for the dirn of rotation
#this is implemented by identifying the elements which will stay & which will leave in array when shifting.
def rotatearay(a1,r):
    di=int(input('Direction of rotation. Press 1 for left & 2 for right:')) #dirn
    
    a2=list(a1) #dupl list
    l=len(a1) 
    
    r=r%l   #steps count

    if r==0:
        print('resultant array is',a1)
    else:
        if di==2:
            print('di2 right')
            for i in range(0,l-r): #stay
                a2[i+r]=a1[i]
            for j in range(l-r,l): #leave
                print(j-(l-r),j)
                a2[j-(l-r)]=a1[j]
        else:            #if r==1:
            print('di1 left')
            for i in range(r,l): #stay
                a2[i-r]=a1[i]
            for z in range(0,r): #leave
                a2[l-r+z]=a1[z]
                                
    return a2



    
    
