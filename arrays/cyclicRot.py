def solution(A,K):
    P=len(A)#length of array

    for count in range(K):#loops the number of times it should rotate
      lastElement=A[P-1]#gives the last element
      for i in range(P-1,0,-1):#loops through the length of the array rotating to the right
        A[i]=A[i-1]
      A[0]=lastElement# moves the last element to the beginning
    return A
        
A=[3, 8, 9, 7, 6]
print(solution(A,3))
A = [1, 2, 3, 4]
print(solution(A,4))
A = [0, 0, 0]
print(solution(A,1))