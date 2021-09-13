/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    const firstQ = numerator / denominator
    let answer = firstQ >= 0 ? Math.floor(firstQ).toString() : '-' + Math.floor(-firstQ).toString()
    let rest = firstQ >= 0 ? numerator % denominator : -numerator % denominator
    let savedUnderPoint = ''
    let saveQandRs = []

    while (rest) {
        rest *= 10

        let quotient = Math.floor(rest / denominator)
        rest %= denominator
        const index = saveQandRs.findIndex(saveQandR => saveQandR[0] === quotient && saveQandR[1] === rest)

        if (index !== -1) {
            const repeatNums = savedUnderPoint.slice(index)
            answer += '.' + savedUnderPoint.slice(0, index)
            answer += '(' + repeatNums + ')'
            break
        }
        else {
            saveQandRs.push([quotient, rest])
            savedUnderPoint += quotient.toString()
        }

        if (rest === 0)
            answer += '.' + savedUnderPoint
    }

    return answer
};