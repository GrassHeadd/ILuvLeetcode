class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        if len(nums1) == 0:
            return [[],nums2]
        if len(nums2) == 0:
            return [[nums1], []]

        numA = []
        numB = []
        dict1 = {}
        dict2 = {}
        #added i to dictionary
        for i in range(len(nums1)):
            if nums1[i] not in dict1:
                dict1.update({nums1[i]: nums1[i]})

        for i in range(len(nums2)):
            if nums2[i] not in dict2:
                dict2.update({nums2[i]: nums2[i]})
        
        for i in range(len(nums2)):
            if nums2[i] not in dict1:
                dict1.update({nums2[i]:nums2[i]})
                numB.append(nums2[i])

        for i in range(len(nums1)):
            if nums1[i] not in dict2:
                dict2.update({nums1[i]:nums1[i]})
                numA.append(nums1[i])
        return [numA, numB]