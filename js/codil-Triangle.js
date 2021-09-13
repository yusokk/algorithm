function solution(A) {
    if (A.length < 3) return 0
    A.sort((a, b) => a-b)
    for (let i = 2; i < A.length; i++) {
        if(A[i-2] + A[i-1] > A[i]) return 1
    }
    return 0
}