class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
        - 2 nested for loop check - O(N*M)
        - sort and  2 pointer - exhaust both approach
        - utilize a hash map to count the occurrences of each element in both arrays.
        '''
        nums1.sort()
        nums2.sort()
        
        result = []
        p1 = p2 = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p2 += 1
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
            
        
        return result
    
    """
    Hash map solution -
        # Create a dictionary to count the occurrences of each element in nums1
    count = {}
    for num in nums1:
        count[num] = count.get(num, 0) + 1

    result = []
    # Iterate through nums2
    for num in nums2:
        # Check if the current number exists in the count dictionary
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result
    """
                
            
            