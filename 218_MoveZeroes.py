'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

def MoveZeroes(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            
            if nums[i]==0 and nums[j]!=0:

                #temp=nums[i]
                #nums[i]=nums[j]
                #nums[j]=temp

                nums[i] , nums[j] = nums[j] , nums[i]



    return nums





nums = [0,1,0,3,12]



#nums = [0]


print(MoveZeroes(nums))

