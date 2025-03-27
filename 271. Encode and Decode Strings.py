class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        # Pattern : "{length of s}#{s}"
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans     

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            # Find the length of sub string s
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # {length of sub string s}#{sub string s}
            # position of i is at #
            i = j + 1
            j = i + length
            ans.append(s[i:j]) 

            # Next iteration
            i = j
        return ans