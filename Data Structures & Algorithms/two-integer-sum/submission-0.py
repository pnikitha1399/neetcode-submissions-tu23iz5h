class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums):
            c = target - n
            if c in hmap:
                return [hmap[c],i]
            hmap[n] = i
