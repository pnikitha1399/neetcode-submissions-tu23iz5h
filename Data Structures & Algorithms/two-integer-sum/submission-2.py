class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        hmap = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hmap:
                return [hmap[c], i]
            hmap[nums[i]] = i
