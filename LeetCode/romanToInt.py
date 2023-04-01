class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        dicnum = {'I':1, "V": 5, 'X':10, 'L':50, "C": 100, 'D':500, "M": 1000}
        for ind, letter in enumerate(s):
            if letter not in 'IXC':
                count+=dicnum[letter]
                continue
            if letter == "I":
                if ind<len(s)-1:
                    if s[ind+1] in "VX":
                        count-=1  
                    else:
                        count+=dicnum[letter]
                else:
                    count+=dicnum[letter]
            elif letter == "X":
                if ind<len(s)-1:
                    if s[ind+1] in "LC":
                        count-=10  
                    else:
                        count+=dicnum[letter]
                else:
                    count+=dicnum[letter]
            elif letter == "C":
                if ind<len(s)-1:
                    if s[ind+1] in "DM":
                        count-=100  
                    else:
                        count+=dicnum[letter]
                else:
                    count+=dicnum[letter]
        return count
            