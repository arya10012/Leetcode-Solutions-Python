# LeetCode 3. Longest Substring Without Repeating Characters
# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # To store last index of characters
        left = 0         # Left pointer of the window
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move left to one position right of the last duplicate
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
