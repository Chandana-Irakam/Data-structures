#linear search using python
def LinearSearch(arr,n,x):
  if n<0:
    return -1
  if arr[n]==x:
    return n
  return LinearSearch(arr,n-1,x)
arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
  j=int(input("Enter numbers for the array:"))
  arr.append(j)
print("Array:",arr)
x=int(input("Enter the target element to search:"))
result=LinearSearch(arr,len(arr)-1,x)
if result!=-1:
  print("Element present at index:",result)
else:
  print("Element is not present in array")
