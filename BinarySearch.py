#binary search using python
def BinarySearch(arr,low,high,x):
  while low<=high:
    mid=low+(high-low)//2
    if arr[mid]==x:
      return mid
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return -1
arr=[]
n=int(input("Enter size of array:"))
for i in range(n):
  k=int(input("Enter elements"))
  arr.append(k)
print("Array",arr)
x=int(input("Enter target element"))
result=BinarySearch(arr,0,n-1,x)
if result!=-1:
  print("Element present at index",result)
else:
  print("Element is not present in array")
