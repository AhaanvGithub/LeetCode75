class Solution(object):
    def runningSum(self, nums):
        l = []
        
        for i in range(len(nums)):
            l += [sum(nums[:i + 1])]
            
        return l
