class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
    
        
        [[10,2],[8,4],[5,1],[3,3],[0,1]]
        
        - sort desending combined array of position and speed
        - check time to reach destination if > curr time then +1 fleet
        
        """
        
        
        fleets = [[p,s] for p,s in zip(position,speed)]
        
        fleets.sort(reverse=True)
        
        no_of_fleet = 0
        curr_time = 0
        
        for fleet in fleets:
            p, s = fleet
            
            time_to_destination = (target - p) / s
            
            if time_to_destination > curr_time:
                no_of_fleet += 1
                curr_time = time_to_destination
            
        return no_of_fleet
                
            
            
        

                
        