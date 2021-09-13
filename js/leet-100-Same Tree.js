/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    const stack = [[p, q]]
    while (stack.length !== 0) {
        const [tree1, tree2] = stack.pop()

        if (tree1 === null && tree2 !== null) return false
        if (tree1 !== null && tree2 === null) return false
        if (tree1?.val !== tree2?.val) return false
        if (tree1 !== null && tree2 !== null) {
            stack.push([tree1.left, tree2.left])
            stack.push([tree1.right, tree2.right])
        }
    }
    return true
};