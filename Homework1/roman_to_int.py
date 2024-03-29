class Solution:
    def romanToInt(self, s: str) -> int:
        symb_val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        for i in range(len(s)-1):
            if symb_val[s[i]] < symb_val[s[i + 1]]:
                sum-=symb_val[s[i]]
            else:
                sum+=symb_val[s[i]]
        sum += symb_val[s[-1]]
        return sum
       