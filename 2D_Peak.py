import numpy as np
import operator

class TwoDPeak(object):
	def __init__(self, terrain):
		self.terrain = np.array(terrain)

	def getTerrainSize(self):
		return self.terrain.shape[0]*self.terrain.shape[1]

	def getElement(self, middle_row, middle_col, direction):
		options = { 1: self.terrain[middle_row, middle_col-1],
					2: self.terrain[middle_row-1, middle_col-1],
					3: self.terrain[middle_row-1, middle_col],
					4: self.terrain[middle_row-1, middle_col+1],
					5: self.terrain[middle_row, middle_col+1],
					6: self.terrain[middle_row+1, middle_col+1],
					7: self.terrain[middle_row+1, middle_col],
					8: self.terrain[middle_row+1, middle_col-1],
				}
		return options[direction]

	def sliceTheTerrain(self, middle_row, middle_col, direction):
		options = { 1: self.terrain[:, :middle_col-1],
					2: self.terrain[:middle_row-1, :middle_col-1],
					3: self.terrain[:middle_row-1, :],
					4: self.terrain[:middle_row-1, middle_col+1:],
					5: self.terrain[:, middle_col+1:],
					6: self.terrain[middle_row+1:, middle_col+1:],
					7: self.terrain[middle_row+1:, :],
					8: self.terrain[middle_row+1:, :middle_col-1],
				}
		self.terrain = options[direction]
		return

	def displayTerrain(self):
		for i in range(self.terrain.shape[0]):
			for j in range(self.terrain.shape[1]):
				print self.terrain[i,j]," "
			print ""
		print "##########"
		
	def findPeak(self):
		if self.getTerrainSize<=4:
			return 
		self.displayTerrain()
		middle_row = (self.terrain.shape[0])/2
		middle_col = (self.terrain.shape[1])/2

		if self.getTerrainSize()<=4:
			print "peak ==> ", max(self.terrain)


		if middle_row==0 and middle_col==0:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [5,6,7]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()


		elif middle_row==0 and middle_col==self.terrain.shape[1]-1:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [1,8,7]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==self.terrain.shape[0]-1 and middle_col==0:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [3,4,5]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==self.terrain.shape[0]-1 and middle_col==self.terrain.shape[1]-1:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [8,6,7]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==0:	
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [1,8,7]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==self.terrain.shape[0]-1:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [2,3,4]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_col==0:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [4,5,6]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_col==self.terrain.shape[1]-1:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [2,1,8]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		else:
			neighbors = {a: self.getElement(middle_row, middle_col, a) for a in [1,2,3,4,5,6,7,8]}
			max_val = max(neighbors.values())
			if self.terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()


plot = [
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]

terrain = TwoDPeak(plot)
terrain.findPeak()









