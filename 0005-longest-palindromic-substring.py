class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        even_answer = self.search_even_answer(s)
        odd_answer = self.search_odd_answer(s)
        
        if len(even_answer) >= len(odd_answer):
            return even_answer
        else:
            return odd_answer

    def search_even_answer(self, s):
        longest_answer = ''
        index = 0
        while index < len(s):
            answer = s[index]
            left_index = index - 1
            right_index = index + 1
            while left_index >= 0 and right_index < len(s):
                if s[left_index] == s[right_index]:
                    answer = s[left_index] + answer + s[right_index]
                    left_index -= 1
                    right_index += 1
                else:
                    break

            if len(answer) > len(longest_answer):
                longest_answer = answer

            index += 1

        return longest_answer


    def search_odd_answer(self, s):
        longest_answer = ''

        index = 1
        while index < len(s):
            answer = ''
            left_index = index - 1
            right_index = index
            while left_index >= 0 and right_index < len(s):
                if s[left_index] == s[right_index]:
                    answer = s[left_index] + answer + s[right_index]
                    left_index -= 1
                    right_index += 1
                else:
                    break

            if len(answer) > len(longest_answer):
                longest_answer = answer

            index += 1

        return longest_answer
