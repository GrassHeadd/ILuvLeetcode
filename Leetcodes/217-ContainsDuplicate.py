class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #use dictionary to check each entry, if contains, return True, else false

        if len(nums) == 1 or len(nums) == 0:
            return False

        thisDict = {}
        for i in range(len(nums)):
            if nums[i] in thisDict: #values would have exceeded
                return True
            else:
                thisDict.update({nums[i]:nums[i]})
        return False
        