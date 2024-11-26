'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

'''

def ContainsDuplicate(nums):
    for i in range(len(nums)):
        if i==len(nums)-1:
            return False
        for j in range(i+1 ,len(nums)):
            if nums[i]==nums[j]:
                return True
        

nums=[1,2,3,1]
nums1=[1,2,3,4]

print(ContainsDuplicate(nums))