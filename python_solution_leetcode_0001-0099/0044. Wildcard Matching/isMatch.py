class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = p_ptr = 0
        star_idx = s_tmp = -1
        
        while s_ptr < len(s):

            if p_ptr < len(p) and p[p_ptr] in {s[s_ptr], '?'}:
                s_ptr += 1
                p_ptr += 1
        
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp = s_ptr
                p_ptr += 1

            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp += 1
                s_ptr = s_tmp
        
            else:
                return False
        
      
        return all(x == '*' for x in p[p_ptr:])