class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            sum_two_numbers = numbers[p1] + numbers[p2]

            if sum_two_numbers > target:
                p2 -= 1
            elif sum_two_numbers < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]

        # If no solution is found, return an empty list or raise an error.
        return []  # or raise ValueError("No solution found.")
            
            
                