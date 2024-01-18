class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        # Base Case 
        costMap = {}
        costMap[0] = cost[0]
        costMap[1] = cost[1]

        for i in range(2, n):
            costMap[i] = min(costMap[i - 1], costMap[i - 2]) + cost[i]
        
        return min(costMap[n-1], costMap[n-2])
        