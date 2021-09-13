/**
 * @param {number[][]} graph
 * @return {boolean}
 */

var isBipartite = function(graph) {
    const setArr = new Array(graph.length).fill(0)

    const dfs = (u, setNo) => {
        let flag = true
        setArr[u] = setNo
        for (let v of graph[u]) {
            if (!flag) break
            if (!setArr[v]) {
                if (setNo === 1) flag = dfs(v, 2)
                else flag = dfs(v, 1)
            }
            else if (setArr[v] === setNo) return false
        }
        return flag
    }

    for (let u = 0; u < graph.length; u++) {
        if (setArr[u].length !== 0 && !setArr[u])
            if (!dfs(u, 1))
                return false
    }
    return true
};