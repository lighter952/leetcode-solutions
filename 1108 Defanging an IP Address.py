class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans: str = ''
        for c in address:
            if c == '.':
                ans += '[.]'
            else:
                ans += c
        return ans