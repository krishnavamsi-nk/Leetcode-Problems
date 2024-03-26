class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        candidate_3 = float('-inf')  # Initialize the candidate for "3" as negative infinity.

        for num in reversed(nums):
            if num < candidate_3:
                return True
            while stack and num > stack[-1]:
                candidate_3 = stack.pop()
            stack.append(num)

        return False

