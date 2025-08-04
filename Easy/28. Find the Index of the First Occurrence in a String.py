class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle
        if not needle:
            return 0

        # Use sliding window to compare substrings
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
