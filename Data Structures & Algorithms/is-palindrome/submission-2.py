class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        for i in range(len(new) // 2):
            if new[i] != new[len(new) - 1 - i]:
                return False

        return True