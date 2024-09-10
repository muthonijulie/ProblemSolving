def reverse(A):
   N = len(A)
   for i in range(N // 2):
     k = N - i - 1
     A[i], A[k] = A[k], A[i]
   return A

A=[4,3,2,1,7,8,9]
print(reverse(A))