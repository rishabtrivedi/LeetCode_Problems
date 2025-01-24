
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        hashMap = {}
        result  = 0
        for right in range(n):
            if s[right] in hashMap:
                hashMap[s[right]] += 1
                while hashMap[s[right]] > 1:
                    hashMap[s[left]] -=1
                    left +=1

            else:
                hashMap[s[right]] = 1
            
            # print(hashMap)
            result = max(result,right-left+1)
        
        return result

            
            
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = Counter()
#         left = 0
#         maxlength = 0 
#         for right in range(len(s)):
            
#             chars[s[right]] += 1
            
#             while chars[s[right]] > 1:
#                 chars[s[left]] -= 1
#                 left +=1
            
#             maxlength = max(maxlength,right - left +1)

#         return maxlength



"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""