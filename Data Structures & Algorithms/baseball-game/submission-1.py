class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i] == "+":
                temp_first_op = int(res.pop())
                temp_second_op = int(res.pop())

                res.append(temp_second_op)
                res.append(temp_first_op)
                res.append(temp_first_op + temp_second_op)

            elif operations[i] == "C":
                res.pop()

            elif operations[i] == "D":
                previous = int(res[-1])
                res.append(previous * 2)
            
            else: 
                new_value = int(operations[i])
                res.append(new_value)

        return sum(res)  



        