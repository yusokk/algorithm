function solution(S, P, Q) {
    const prefixSum = []
    const answer = []

    for (let i = 0; i < S.length; i++) {
        const num = stringToNum(S[i])
        let lastSum

        if (i === 0) lastSum = [0, 0, 0, 0]
        else lastSum = [...prefixSum[i-1]]

        lastSum[num-1] += 1
        prefixSum.push(lastSum)
    }

    for (let i = 0; i < P.length; i++) {
        const [start, last] = [P[i]-1, Q[i]]
        let answerNum = 0

        if (start === -1) {
            answerNum = findMin( prefixSum[last] )
            answer.push(answerNum)
        }
        else {
            const answerArr = prefixSum[last].map( (x, i) => {
                return x - prefixSum[start][i]
            })

            answerNum = findMin(answerArr)
            answer.push(answerNum)
        }
    }

    return answer
}

function stringToNum(string) {
    switch (string) {
        case 'A':
            return 1
        case 'C':
            return 2
        case 'G':
            return 3
        case 'T':
            return 4
    }
}

function findMin(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] !== 0) return i+1
    }
}