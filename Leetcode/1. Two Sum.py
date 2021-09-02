###### 방법 1 Runtime : 1035ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            if target-i in nums and idx != nums.index(target-i):
                return sorted([idx, nums.index(target-i)])


#-----------------------------------------------------------------------


###### 방법 2 Runtime : 103ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for idx, i in enumerate(nums):
            if target-i in hashmap:
                return [hashmap[target-i], idx]
            hashmap[i]=idx
            
            