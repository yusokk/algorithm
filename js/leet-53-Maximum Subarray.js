/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = Math.max(...nums)
    let tempSum = 0
    for (let i = 0; i < nums.length; i++) {
        tempSum += nums[i]
        if (maxSum < tempSum) maxSum = tempSum
        if (tempSum < 0) tempSum = 0
    }
    return maxSum
};