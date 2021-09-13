function solution(A, B, K) {
    const start = Math.ceil(A / K)
    const last = Math.floor(B / K)

    return last - start + 1
}