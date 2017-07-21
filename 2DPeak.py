import numpy as np
import operator

class 2DPeak(object):
	def __init__(self, terrain):
		self.terrain = np.array(terrain)

	def getTerrainSize(self):
		return len(self.terrain[0])*len(self.terrain[0][0])

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

	def findPeak(self):
		if getTerrainSize<=4:
			return 
		middle_row = (self.terrain.shape[0])/2
		middle_col = (self.terrain.shape[1])/2

		if self.getTerrainSize<=4:
			print "peak ==> ", max(self.terrain)


		if middle_row==0 and middle_col==0:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [5,6,7]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()


		elif middle_row==0 and middle_col==len(self.terrain[0][0])-1:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [1,8,7]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==len(self.terrain[0])-1 and middle_col==0:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [3,4,5]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==len(self.terrain[0])-1 and middle_col==len(self.terrain[0][0])-1:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [8,6,7]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==0:	
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [1,8,7]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_row==len(self.terrain[0])-1:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [2,3,4]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_col==0:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [4,5,6]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		elif middle_col==len(self.terrain[0][0])-1:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [2,1,8]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()

		else:
			neighbors = {a: getElement(middle_row, middle_column, a) for a in [1,2,3,4,5,6,7,8]}
			max_val = max(neighbors.values)
			if terrain[middle_row,middle_col]>max_val:
				print "peak ==> ", self.terrain[middle_row, middle_col]
			self.sliceTheTerrain(middle_row, middle_col, max(neighbors, key=lambda key: neighbors[key]))
			self.findPeak()











