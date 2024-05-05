class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
        return l
        