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

const dfs = (node, depth) => {
    if (node === null) return [true, depth]
    let [rightFlag, rightDepth] = dfs(node.right, depth+1)
    let [leftFlag, leftDepth] = dfs(node.left, depth+1)
    if (!rightFlag || !leftFlag) return [false, 0]
    if (Math.abs(rightDepth - leftDepth) > 1) return [false, 0]
    return [true, Math.max(leftDepth, rightDepth)]
}

var isBalanced = function(root) {
    let depth = 0
    let flag = true

    if (root === null) return true
    else [flag, depth] = dfs(root, 0)

    return flag
};