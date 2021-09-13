/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((a, b) => b - a)
    let answer = 0
    for (let i = 0; i < citations.length; i++) {
        const h = i+1
        if (citations[i] >= h)
            if (h !== citations.length){
                if (citations[h] <= h){
                    answer = h
                }
            }
            else answer = h
    }
    return answer
};