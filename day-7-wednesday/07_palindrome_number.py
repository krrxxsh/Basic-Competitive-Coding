class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


solver = Solution()
print(solver.isPalindrome(121))
print(solver.isPalindrome(-121))


