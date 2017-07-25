s = [1,2,3,4,4,5,6,3,2,1,3]


class OneDPeak(object):
	def __init__(self, terrain):
		self.terrain = terrain

	def find_peak(self, start, end):
		middle = (start+end)/2
		if self.terrain[middle-1]<=self.terrain[middle] and self.terrain[middle+1]<=self.terrain[middle]:
			print self.terrain[middle]
			return
		if start==end:
			print self.terrain[start]
			return
		if end==start+1:
			print max(self.terrain[start], self.terrain[end])
			return
		else:
			if self.terrain[middle]>self.terrain[middle-1] and self.terrain[middle]<=self.terrain[middle+1]:
				self.find_peak(middle+1, end)
			else:
				self.find_peak(start, middle-1)


terrain = OneDPeak(s)
terrain.find_peak(0,len(s)-1)