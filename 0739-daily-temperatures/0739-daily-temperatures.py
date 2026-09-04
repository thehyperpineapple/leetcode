class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                StackT, StackInd = stack.pop()
                output[StackInd] = (i-StackInd)
            stack.append([t,i])
        return output