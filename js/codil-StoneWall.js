function solution(H) {
    const stack = []
    let count = 0
    for (let h of H) {
        if (stack.length !== 0 && stack[stack.length-1] === h) continue
        if (stack.length === 0) {
            stack.push(h)
            continue
        } 
        while (stack.length > 0 && h <= stack[stack.length-1]) {
            const popH = stack.pop()
            if (h < popH) count++
        }
        stack.push(h)
    }
    count += stack.length
    return count
}