n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp_str = ""
        for j in range(n-1, -1, -1):
            temp = arr1[i] & (1<<j) | arr2[i] & (1<<j)
            temp_str += "#" if temp == (1<<j) else " "
        answer.append(temp_str)
    return answer

solution(n, arr1, arr2)