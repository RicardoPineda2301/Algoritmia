Lista = [16,14,10,8,7,9,3,2,4,1]

def esHeap(A):
    for i in range (0, len(A)):
        if (A[2*i +1] > A[i]):
                return False
 
        if (A[2*i+2] > A[i]):
                return False
    return True

esHeap(Lista)