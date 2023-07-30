class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trackMap = {}
        result = []
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            
            if trackMap.get(sortedS) == None :
                trackMap[sortedS] = [s]
            else:
                trackMap[sortedS].append(s)
                
            
        for v in trackMap.values():
            result.append(v)
            
        return result
            

                
                