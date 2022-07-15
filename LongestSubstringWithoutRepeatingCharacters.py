class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        substr = ""
        letters = set()
        substrings = []
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in letters:
                    substr += s[j]
                    letters.add(s[j])
                else:
                    break

            letters.clear()
            substrings.append(len(substr))
            substr = ""
        return max(substrings)
