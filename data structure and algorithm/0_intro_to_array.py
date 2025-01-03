li=[]
li.append(12)
li.append("sam")
li.append(1.2)
print(li) #but in array it is having same data type.
# help()

import array 
arr = array.array('i',[1,2,3,4,5])
print(arr)
arr[0] = 10
print(arr) 