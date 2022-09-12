class Solution(object):
    def isIsomorphic(self, s, t):
        s_keyvalues = {}
        t_keyvalues = {}
        
        for i in range(len(s)):
            if s[i] in s_keyvalues:
                if s_keyvalues[s[i]] != t[i]:
                    return False
            elif t[i] in t_keyvalues:
                if t_keyvalues[t[i]] != s[i]:
                    return False
            else:
                s_keyvalues[s[i]] = t[i]
                t_keyvalues[t[i]] = s[i]
                
        return True
