#Linear search using recurssion
def Linear(arr,n,k):
    if arr[n]==k:
        return 'found'
    if n==len(arr)-1:
        return 'not found'
    return Linear(arr,n+1,k)
arr=[1,2,3,4,10,3,4,78]
print(Linear(arr,0,10))

#Binary Search using Recurssion
def Binarysearch(arr,l,r,k):
    mid=(l+r)//2
    if arr[mid]==k:
        return 'found'
    elif k<arr[mid]:
        return Binarysearch(arr,l,mid-1,k)
    elif k>arr[mid]:
        return Binarysearch(arr,mid+1,r,k)
    return 'not found'
arr1=[1,2,3,4,5,6,7,8,9,10]
aar1=sorted(arr1)
n=len(arr1)
print(Binarysearch(arr1,0,n,7))