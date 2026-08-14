class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_map = {}
        t_char_map = {}

        for c in range(len(s)):
            if s[c] in s_char_map:
                s_char_map[s[c]] += 1
            else:
                s_char_map[s[c]] = 1

            if t[c] in t_char_map:
                t_char_map[t[c]] += 1
            else:
                t_char_map[t[c]] = 1

        for c in range(len(s)):
            s_char = s[c]
            if s_char not in s_char_map or s_char not in t_char_map:
                return False
            if s_char_map[s_char] != t_char_map[s_char]:
                return False

        return True
