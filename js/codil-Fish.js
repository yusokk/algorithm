function solution(A, B) {
    let count = 0
    const downStream = []

    for (let i = 0; i < A.length; i++) {
        if (B[i] === 1) {
            downStream.push(i)
            continue
        }
        while (downStream.length !== 0) {
            const downFish = downStream[downStream.length-1]
            if (A[downFish] > A[i])
                break
            else
                downStream.pop()
        }
        if (downStream.length === 0) count++
    }

    count += downStream.length

    return count
}