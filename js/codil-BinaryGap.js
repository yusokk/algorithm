function solution(N) {
    binaryN = N.toString(2)
    let answer = 0
    let count = 0
    for (let num of binaryN) {
        if (num === '1') {
            if (count > answer) answer = count
            count = 0
        }
        else count++
    }
    return answer
}