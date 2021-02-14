test = input().split()
input_A = test[0]
input_B = test[1]
str_A = input_A[2] + input_A[1] + input_A[0]
str_B = input_B[2] + input_B[1] + input_B[0]
A = int(str_A)
B = int(str_B)
if A > B:
    print(A)
else:
    print(B)