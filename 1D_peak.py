s = [1,2,3,4,4,5,6,3,2,1,3]


class OneDPeak(object):
	def __init__(self, terrain):
		self.terrain = terrain
		
def find_peak(a, start, end):
	middle = (start+end)/2
	if a[middle-1]<=a[middle] and a[middle+1]<=a[middle]:
		print a[middle]
		return
	if start==end:
		print a[start]
		return
	if end==start+1:
		print max(a[start], a[end])
		return
	else:
		if a[middle]>a[middle-1] and a[middle]<=a[middle+1]:
			find_peak(a, middle+1, end)
		else:
			find_peak(a, start, middle-1)

find_peak(s,0,len(s)-1)