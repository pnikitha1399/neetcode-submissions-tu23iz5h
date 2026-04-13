class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hmap:
                return [hmap[c],i]
            hmap[nums[i]]=i
