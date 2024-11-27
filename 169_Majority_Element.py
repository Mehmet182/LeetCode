'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

'''
def Majority_element(nums):
    nums2=[]
    enbuyuk2=nums[0]
    for c in range(len(nums)):
        if enbuyuk2<nums[c]:
            enbuyuk2=nums[c]
            index2=c

    for j in range(enbuyuk2+1):
        nums2.append(0)

    for i in range(len(nums)):
        nums2[nums[i]]=nums2[nums[i]]+1

    enbuyuk=nums2[0] 
    index="belirsiz"   
    for k in range(len(nums2)):
        if enbuyuk<nums2[k]:
            enbuyuk=nums2[k]
            index=k
    if enbuyuk==1 and k==len(nums2):
        print("no most recurring value")
    else:
        print("most common element={}".format(index))
            
#print(nums2)
nums2=[2,2,1,1,1,2,2]
nums3=[3,2,3]
nums=[5,6,9,4,1,1,5,40,40,40,40]
Majority_element(nums)
