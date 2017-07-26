'''
Class Sort has different sort methods.
Call and compare the time required to complete the sorting using different methods
'''

import time
import random

class Sort(object):
	def __init__(self, l):
		self.l = l

	def insertionSort(self):
		start = time.clock()
		for i in range(1,len(self.l)):
			key = self.l[i]
			for searchIndex in range(i-1,-1,-1):
				if self.l[searchIndex]<key:
					break
				else:
					temp = self.l[searchIndex]
					self.l[searchIndex] = key
					self.l[searchIndex+1] = temp
		end = time.clock()
		print 'Time in seconds required to complete the sorting ==>', end-start

	def displayList(self):
		print self.l

s = [random.randint(-100,100) for i in xrange(1000)]

sort = Sort(s)
sort.insertionSort()
sort.displayList()
