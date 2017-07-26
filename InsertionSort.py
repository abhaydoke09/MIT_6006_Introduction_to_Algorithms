class Sort(object):
	def __init__(self, l):
		self.l = l

	def insertionSort(self):
		for i in range(1,len(self.l)):
			key = self.l[i]
			for searchIndex in range(i-1,-1,-1):
				if self.l[searchIndex]<key:
					break
				else:
					temp = self.l[searchIndex]
					self.l[searchIndex] = key
					self.l[searchIndex+1] = temp

	def displayList(self):
		print self.l

s = [10,-5,5,6,1,3]
sort = Sort(s)
sort.insertionSort()
sort.displayList()
