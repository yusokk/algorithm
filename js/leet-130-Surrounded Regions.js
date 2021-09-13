/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */

const directions = [1, -1, 0, 0]


const solve = function(board) {

    const m = board.length
    const n = board[0].length
    const check = []
    const stack = []

    const dfs = (i, j) => {
        if (board[i][j] === 'O') {
            stack.push([i, j])
            while (stack.length !== 0) {
                let [r, c] = stack.pop()
                check.push([r, c])
                board[r][c] = 'X'
                for (let k = 0; k < 4; k++) {
                    const nextR = r + directions[k]
                    const nextC = c + directions[3-k]
                    if (0 <= nextR && nextR < m && 0 <= nextC && nextC < n) {
                        if (board[nextR][nextC] === 'O')
                            stack.push([nextR, nextC])
                        }
                    }
                }
            }
        }

    for (let i = 0; i < m; i++) {
        dfs(i, 0)
        dfs(i, n-1)
    }
    for (let i = 1; i < n-1; i++) {
        dfs(0, i)
        dfs(m-1, i)
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') board[i][j] = 'X'
        }
    }

    for (let index = 0; index < check.length; index++) {
        board[check[index][0]][check[index][1]] = 'O'
    }
};