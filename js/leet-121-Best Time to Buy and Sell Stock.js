/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxPrice = 0
    let minPrice = prices[0]
    let maxProfit = 0
    for (let i = 0; i < prices.length; i++) {
        if (maxPrice < prices[i]) maxPrice = prices[i]
        if (prices[i] < minPrice) {
            if (maxProfit < maxPrice - minPrice) maxProfit = maxPrice - minPrice
            minPrice = prices[i]
            maxPrice = prices[i]
        }
    }
    if (maxProfit < maxPrice - minPrice) maxProfit = maxPrice - minPrice
    return maxProfit
};