class Solution:

    
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        count = 0
        greed = sorted(g)
        size = sorted(s)
        g_ptr = 0
        s_ptr = 0

        while s_ptr < len(size) and g_ptr < len(greed):

            if size[s_ptr] >= greed[g_ptr]:
                count += 1
                s_ptr += 1
                g_ptr += 1

            else:
                s_ptr += 1

        return count