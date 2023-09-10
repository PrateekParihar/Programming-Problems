class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        
        for c,p in prerequisites:
            adj[c].append(p)
            
        visit = [0] * numCourses
        
        def hasCycle(course):
            
            if visit[course] == 1:
                return True
            
            if visit[course] == 2:
                return False
            
            visit[course] = 1
            
            for pre in adj[course]:

                if hasCycle(pre):
                    return True
        
            visit[course] =2
            
            return False
        
        for c in range(numCourses):
            if hasCycle(c):
                return False
        return True        
        
            
        
        