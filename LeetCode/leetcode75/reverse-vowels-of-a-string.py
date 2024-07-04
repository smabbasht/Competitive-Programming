class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        left = False
        right = False
        vowels = "AEIOUaeiou"
        s_ = list(s)
        while i <= j:
            if s[i] in vowels:
                left = True
            else:
                i += 1

            if s[j] in vowels:
                right = True
            else:
                j -= 1

            if left and right:
                s_[i], s_[j] = s_[j], s_[i]
                left = False
                right = False
                i += 1
                j -= 1

        return "".join(s_)
