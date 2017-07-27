def mergeSort(a):
	if len(a):
		return
	else:
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


print merge([2],[3])



