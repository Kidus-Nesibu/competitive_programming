from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_map = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        unique_representations = set()
        
        for word in words:
            morse_word = "".join(morse_map[ord(c) - ord('a')] for c in word)
            unique_representations.add(morse_word)
        
        return len(unique_representations)
