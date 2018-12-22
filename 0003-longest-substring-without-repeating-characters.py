class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_string_length = 0
        
        string = ''
        for c in s:
            index = string.find(c)
            if index == -1:
                string += c
                continue

            longest_string_length = max(longest_string_length, len(string))
            string = string[index + 1:] + c

        longest_string_length = max(longest_string_length, len(string))

        return longest_string_length
