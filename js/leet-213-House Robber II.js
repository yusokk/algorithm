/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const dpWithFirst = Array.from({length: nums.length}, () => 0)
    const dpWithoutFirst = Array.from({length: nums.length}, () => 0)

    for (let i = 0; i < nums.length; i++) {
        if (0 <= i-3) {
            if (i !== nums.length-1){
                if (dpWithFirst[i-3] < dpWithFirst[i-2])
                    dpWithFirst[i] = dpWithFirst[i-2] + nums[i]
                else dpWithFirst[i] = dpWithFirst[i-3] + nums[i]
            }

            if (dpWithoutFirst[i-3] < dpWithoutFirst[i-2])
                dpWithoutFirst[i] = dpWithoutFirst[i-2] + nums[i]
            else dpWithoutFirst[i] = dpWithoutFirst[i-3] + nums[i]
        }
        else if (i === 2) {
            if (i !== nums.length-1) {
                dpWithFirst[i] = dpWithFirst[i-2] + nums[i]
                dpWithoutFirst[i] = dpWithoutFirst[i-2] + nums[i]
            }
            else
                dpWithoutFirst[i] = dpWithoutFirst[i-2] + nums[i]
        }
        else {
            if (i === 0)
                dpWithFirst[i] = nums[i]
            else
                dpWithoutFirst[i] = nums[i]
        }
    }

    dpWithFirst.sort((a, b) => a-b)
    dpWithoutFirst.sort((a, b) => a-b)
    let maxMoney = dpWithFirst[nums.length-1]
    if (dpWithFirst[nums.length-1] < dpWithoutFirst[nums.length-1])
        maxMoney = dpWithoutFirst[nums.length-1]
    return maxMoney
};