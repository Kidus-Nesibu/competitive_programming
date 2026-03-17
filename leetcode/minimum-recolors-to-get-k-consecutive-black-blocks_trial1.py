class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count_white = 0
        min_recolor = k
        
        for i in range(k):
            if blocks[i] == 'W':
                count_white += 1
        
        min_recolor = count_white
        
        for i in range(k, n):
            if blocks[i - k] == 'W':
                count_white -= 1
            if blocks[i] == 'W':
                count_white += 1
            if count_white < min_recolor:
                min_recolor = count_white
        
        return min_recolor