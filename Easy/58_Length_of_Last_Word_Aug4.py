<<<<<<< HEAD
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
=======
# Leetcode 58. Length of Last Word
# Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces, then split into words
        words = s.strip().split()
        return len(words[-1])
>>>>>>> 7a05a771c78a6faa23b2f4991c32f86cb0d13192
