#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        i = 0
        word = ''
        maxlen = 0
        
        while i < len(s):
            j = i + 1
            word = s[i]
            while j < len(s):
                #print(i, j, word)
                if s[j] in word:
                    #print(s[j])
                    if len(word) > maxlen:
                        maxlen = len(word)
                    break
                else:
                    word += s[j]
                j += 1
            if len(word) > maxlen:
                maxlen = len(word)
            i += 1
        return maxlen