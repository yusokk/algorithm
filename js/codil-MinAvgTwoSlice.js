function solution(A) {
    let minTwo = [0, 10000]
    let minTree = [0, 10000]

    for (let i = 0; i < A.length; i++) {
        if (i < A.length - 1) {
            const average = (A[i] + A[i+1]) / 2
            if (average < minTwo[1]) minTwo = [i, average]
        }

        if (i < A.length - 2) {
            const average = (A[i] + A[i+1] + A[i+2]) / 3
            if (average < minTree[1]) minTree = [i, average]
        }
    }

    if (minTwo[1] < minTree[1]) return minTwo[0]
    else if (minTwo[1] === minThree[1] && minTwo[0] < minThree[0]) return minTwo[0]
    else return minTree[0]
}

// 40% ㅠㅠ