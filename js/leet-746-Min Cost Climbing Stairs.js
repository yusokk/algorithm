/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    const length = cost.length
    const dp = Array(length)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for (let i = 2; i < length; i++) {
        dp[i] = Math.min(dp[i-1], dp[i-2]) + cost[i]
    }
    return Math.min(dp[length-1], dp[length-2])
};