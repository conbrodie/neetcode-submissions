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

        return s_char_map == t_char_map
