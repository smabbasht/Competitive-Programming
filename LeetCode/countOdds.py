class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high_inc, low_inc = (high%2==1)*1, (low%2==1)*1
        return ((high+high_inc)-(low-low_inc))//2