class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        x = set()
        for i in range(len(s) - 9):
            if s[i:i+10] in dic:
                x.add(s[i:i+10])
            else:
                dic[s[i:i+10]] = 1
        return x
