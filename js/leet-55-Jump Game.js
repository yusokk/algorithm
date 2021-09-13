/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let index = 0
    let maxIndex = 0
    while (index <= maxIndex && index < nums.length) {
        const next = nums[index] + index
        if (maxIndex < next) maxIndex = next
        if (nums.length-1 <= maxIndex) return true
        index++
    }
    return false
};