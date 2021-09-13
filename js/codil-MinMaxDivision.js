// 계속 틀린 테스트케이스
//
// medium_zeros
// many zeros and 99 in the middle, length = 15,000
//
// 0을 제외한 숫자의 갯수가 K보다 작거나 같으면 최댓값을 반환시키는 조건 추가

function solution(K, M, A) {
    if (A.length <= K) return Math.max(...A)

    let lengthCnt = 0
    for (let num of A) if (num !== 0) lengthCnt++

    if (lengthCnt <= K) return Math.max(...A)

    let start = 0
    let end = M * A.length
    let mid

    while (start <= end) {
        mid = Math.floor((start + end) / 2)
        let sum = 0
        let count = 0
        for (let num of A) {
            if (sum + num > mid) {
                count += 1
                sum = num
            }
            else sum += num
        }
        if (count >= K) start = mid + 1
        else end = mid - 1
    }
    return start
}