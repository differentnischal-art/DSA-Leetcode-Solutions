class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_length = 0
        characters=set()

        for right in range(len(s)):

            # Remove duplicate characters
            while s[right] in characters:
                characters.remove(s[left])
                left = left + 1

            # Add current character
            characters.add(s[right])

            # Calculate window length
            length = right - left + 1

            if length > max_length:
                max_length = length
        return max_length
                