class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        newCandies = [x + extraCandies for x in candies]
        for x in newCandies:
            if x >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
