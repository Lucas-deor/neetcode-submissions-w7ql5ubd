class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        const stack = []
        let sum = 0

        for (let i = 0; i < operations.length; i++) {
            if (operations[i] === "+") {
                stack.push(Number(stack[stack.length - 1]) + Number(stack[stack.length - 2]))
            } else if (operations[i] === "D") {
                stack.push(Number(stack[stack.length - 1]) * 2)
            } else if (operations[i] === "C") {
                stack.pop()
            } else {
                stack.push(Number(operations[i]))
            }
        }

        for (let j = 0; j < stack.length; j++) {
            sum += stack[j]
        }

        return sum
    }
}
