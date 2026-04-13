class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(len(nums))
        print(len(list(set(nums))))
        if len(nums)==len(list(set(nums))):
            return False
        return True