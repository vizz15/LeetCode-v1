class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list=s.split()
        x=word_list.pop()
        return len(x)
        