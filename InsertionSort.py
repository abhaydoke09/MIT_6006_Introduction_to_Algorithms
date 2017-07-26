def insertionSort(l):
	for i in range(1,len(l)):
		key = l[i]
		for searchIndex in range(i-1,-1,-1):
			if l[searchIndex]<key:
				break
			else:
				temp = l[searchIndex]
				l[searchIndex] = key
				l[searchIndex+1] = temp
	return l

s = [5,4,2,6,1,3]
print insertionSort(s)
