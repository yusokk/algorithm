/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    const leftQue = [root.left]
    const rightQue = [root.right]
    const leftArr = []
    const rightArr = []
    while (leftQue.length !== 0) {
        const popLeftNode = leftQue.shift()
        leftArr.push(popLeftNode !== null ? popLeftNode.val : null)
        if (popLeftNode !== null){
            leftQue.push(popLeftNode.left)
            leftQue.push(popLeftNode.right)
        }
    }
    while (rightQue.length !== 0) {
        const popRightNode = rightQue.shift()
        rightArr.push(popRightNode !== null ? popRightNode.val : null)
        if (popRightNode !== null){
            rightQue.push(popRightNode.right)
            rightQue.push(popRightNode.left)
        }
    }
    for (let i = 0; i < rightArr.length; i++) {
        if (leftArr[i] !== rightArr[i]) return false
    }
    return true
};