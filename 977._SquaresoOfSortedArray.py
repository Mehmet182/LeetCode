'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''

def square(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]

    return(nums)

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                temp =nums[j] 
                nums[j]=nums[j+1]
                nums[j+1]=temp

    return nums



def selection_sort(nums):
    for i in range(len(nums)-1):
        min=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min]:
                min=j

        temp=nums[min]
        nums[min]=nums[i]
        nums[i]=temp

    return nums



nums2 = [-7,-3,2,3,11]
nums =[-4,-1,0,3,10]
print(nums)
print(square(nums))
#print(bubble_sort(nums))
print(selection_sort(nums))