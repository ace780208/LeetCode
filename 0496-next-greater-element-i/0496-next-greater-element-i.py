class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = dict()
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                greater[stack.pop()] = nums2[i]    
            stack.append(nums2[i])
        
        while stack:
            greater[stack.pop()] = -1
        
        return [greater[i] for i in nums1]