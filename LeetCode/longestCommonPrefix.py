class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        strs.sort(key= lambda x: len(x))
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[j][i] !=strs[0][i]:
                    if len(result)==0:
                        return ""
                    else:
                        return "".join(result)
            result.append(strs[0][i])
        
        return "".join(result)