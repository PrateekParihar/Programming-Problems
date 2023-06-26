class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - Two pointer approach
        - Note from Q - The remaining elements of nums are not important as well as the size of nums.
        - Return the numer of unique elements
        '''
        p1 = p2 = result = 0

        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                result += 1

            p2 += 1

        return result + 1        
        
'''
Initialize three pointers: p1, p2, and result.

p1 represents the index of the last unique element encountered so far.
p2 represents the current index being checked for uniqueness.
result keeps track of the count of unique elements.
Start a loop that continues until p2 reaches the end of the nums array.

Inside the loop, check if the element at index p1 is different from the element at index p2.

If they are different, it means a new unique element is found.
Increment p1 by 1 to move it to the next position.

Assign the element at index p2 to the new position determined by p1 in the nums array. This effectively removes duplicates in-place by overwriting them.

Increment result by 1, as we have encountered a new unique element.

Increment p2 by 1 to move to the next element in the array.

Once the loop ends, return result + 1. Adding 1 accounts for the last unique element encountered since result only counts the number of unique elements encountered so far.

The algorithm traverses the nums array with two pointers (p1 and p2). Whenever a new unique element is found, it updates the p1 index and overwrites the duplicate elements in-place. Finally, it returns the count of unique elements.

This solution maintains the relative order of elements as it only modifies the array by removing duplicates, while preserving the order of the unique elements.
'''



                
            
            
        
        
        