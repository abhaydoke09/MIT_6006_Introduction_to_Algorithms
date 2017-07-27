def mergeSort(a):
	if len(a)==1:
		return a
	else:
		start = 0
		end = len(a)
		middle = (start+end)/2
		left = mergeSort(a[start:middle])
		right = mergeSort(a[middle:end])

		return merge(left, right)

def merge(left, right):
	c = []
	leftPointer = 0
	rightPointer = 0
	while(leftPointer != len(left) and rightPointer != len(right)):
		if left[leftPointer] < right[rightPointer]:
			c.append(left[leftPointer])
			leftPointer+=1
		else:
			c.append(right[rightPointer])	
			rightPointer+=1

	if leftPointer==len(left):
		while(rightPointer!=len(right)):
			c.append(right[rightPointer])	
			rightPointer+=1
	elif rightPointer==len(right):
		while(leftPointer!=len(left)):
			c.append(left[leftPointer])
			leftPointer+=1

	return c


s = [3,2,1,4,2,5,7,1,23,4,5,7,8,0]
print mergeSort(s)



