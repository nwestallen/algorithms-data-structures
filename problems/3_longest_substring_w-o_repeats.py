#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        # This solution loops through every index of the string then loops through the rest of the string
        # until a duplicate is found or the end of the string is reached. This has O(n^2) time complexity
        # it checks every substring of s

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        i = 0
        word = set()
        maxlen = 1
        
        while i < len(s) - maxlen:
            j = i + 1
            word = set()
            word.add(s[i])
            while j < len(s) and not s[j] in word:
                word.add(s[j])
                j += 1
            maxlen = max(len(word), maxlen)
            i +=  1
        return maxlen

    def lengthOfLongestSubstring(self, s:str) -> int:
        # This solution uses a sliding window with two pointers - the key for me is that the right pointer will stay
        # to the right rather than reset back to left + 1. Now we visit each index a max 2 times for O(2n) ~> O(n)
        # We expand the window to the right until a duplicate is found, in which case we slide to the left until the 
        # current window no longer contains a repeated character, always comparing the len of the current set to the max thus far

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i = j = 0
        word = set()
        maxlen = 1

        while j < len(s):

            while s[j] in word:
                word.remove(s[i])
                i += 1

            word.add(s[j])

            maxlen = max(maxlen, len(word))
            j += 1

        return maxlen


def test_same_letter():
    assert Solution().lengthOfLongestSubstring('nnnnnnn') == 1

def test_longest_is_repeated():
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3

def test_empty_string():
    assert Solution().lengthOfLongestSubstring('') == 0

def test_longest_overlaps_with_invalid_string():
    assert Solution().lengthOfLongestSubstring('dvdf') == 3

def test_noncontiguous_new_letter():
    assert Solution().lengthOfLongestSubstring('abcdeeefghhh') == 5

def test_repeats_followed_by_longest():
    assert Solution().lengthOfLongestSubstring('aaaaabcde') == 5

def test_duplicate_early_in_string():
    assert Solution().lengthOfLongestSubstring('anviaj') == 5

def test_nasty():
    assert Solution().lengthOfLongestSubstring('abcxxxxabababcdefgggghxxyyyyyyyyyyyyyyyyyyyy') == 7

if __name__ == "__main__":
    test_noncontiguous_new_letter()
   