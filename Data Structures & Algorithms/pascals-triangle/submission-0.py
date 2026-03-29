class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(numRows):
            if i == 0:
                continue

            aux_list = list(output[i - 1])
            output.append(aux_list)
            output[i].append(1)
        
        for i in range(numRows):
            scnd = 1   
            for j in range(len(output[i - 1]) - 1):
                if len(output[i]) == 1 or len(output[i]) == 2:
                    continue
                output[i][scnd] = output[i-1][j] + output[i-1][scnd]
                scnd += 1
        
        return output
