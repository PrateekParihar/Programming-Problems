class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        - Two loops 
        - One to capture occurance
        - Other to get the first unique
        """
        
        track = {}
        
        for ch in s:
            if ch not in track:
                track[ch] = 1
            else:
                track[ch] += 1
        # above can be written in a single line using the dictionary get() method. The get() method of a dictionary returns the value associated with a given key. If the key is not found, it returns the default value provided
        
        # track[ch] = track.get(ch, 0) + 1
                
        for i, ch in enumerate(s):
            if track[ch] == 1:
                return i
            
        return -1
                
        