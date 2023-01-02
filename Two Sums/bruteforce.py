class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute-Force Solution
        index = []
        

        # We want to iterate through the list 
        for i in range(len(nums)-1):
            _sum = 0.0 #Everytime we loop, the sum will reset to 0

            #We will add the element to for each element in the array
            for j in range(i+1,len(nums)):
                _sum = nums[i] + nums[j]
            
                #If the sum is == target, then append the index and index whose sum is = target
                if _sum == target:
                    index.append(i)
                    index.append(j)

        return index    