class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backTrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            else:
                for c in phone[digits[i]]:
                    backTrack(i+1, curr_str+c)
        if len(digits):
            backTrack(0, "")
        return res