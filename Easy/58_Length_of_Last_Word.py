# Leetcode 58. Length of Last Word
# Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces, then split into words
        words = s.strip().split()
        return len(words[-1])
