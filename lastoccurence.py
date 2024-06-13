def lastoccurence(nums,target):
    n=len(nums)
    l,r=0,n-1
   
    result=-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            result=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid+1
    return result
nums = [1, 2, 3, 4, 4, 4, 4, 6, 7]
print(lastoccurence(nums, 4))
print(lastoccurence(nums, 7))
print(lastoccurence(nums, 41))



