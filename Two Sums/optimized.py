class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Optimized Solution
        complement = {} #Lets store the value complimenting an element and the index
        
        # We want to iterate through the array
        for index in range(len(nums)):
            pairNum = 0.0 #Let's find the number that will add to target
            pairNum = target - nums[index]

            #If the number exist in the hash table, we will retrieve the index
            if nums[index] in complement:
                pairIndex = complement[nums[index]]
                return [pairIndex, index]


            #We will store the pairNum to our Hashtable along with the index
            complement[pairNum] = index
