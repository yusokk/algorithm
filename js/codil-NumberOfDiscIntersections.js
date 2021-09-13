function solution(A) {
    const circleArr = []
    for (let i = 0; i < A.length; i++) {
        const r = A[i]
        circleArr.push([i-r, 0]) // 왼쪽 끝
        circleArr.push([i+r, 1]) // 오른쪽 끝
    }

    circleArr.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0]
        }
        else return a[1] - b[1]
    })

    let currentCircles = 0
    let answer = 0

    for (let [_, isEnd] of circleArr) {
        if (isEnd) {
            currentCircles -= 1
        }
        else {
            answer += currentCircles
            currentCircles += 1
            if (answer > 10000000) {
                answer = -1
                break
            }
        }
    }

    return answer
}