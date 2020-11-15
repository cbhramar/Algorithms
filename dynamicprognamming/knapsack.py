class DynamicProgram(object):
	def __init__(self, capacity, weights, values):
		self.capacity, self.weights, self.values, self.dimension = capacity, weights, values, len(weights)
		self.dpMatrix = [[0 for x in range(self.capacity+1)] for y in range(self.dimension+1)]

	def populateMatrix(self):
		for i in range(1, self.dimension+1):
			for w in range(1, self.capacity+1):
				if self.weights[i-1] <= w:
					self.dpMatrix[i][w] = max(self.values[i-1]+self.dpMatrix[i-1][w-self.weights[i-1]], self.dpMatrix[i-1][w])
				else:
					self.dpMatrix[i][w] = self.dpMatrix[i-1][w]

	def head(self):
		return self.dpMatrix[self.dimension][self.capacity]

	def print(self):
		for i in range(self.dimension+1):
			for w in range(self.capacity+1):
				print(str(self.dpMatrix[i][w]), end = '  ')
			print()


def main():
	weights = [1, 4, 2, 3]
	values = [10, 20, 30, 40]
	capacity = 5

	ks = DynamicProgram(capacity, weights, values)
	ks.populateMatrix()
	ks.print()
	print(ks.head())

if __name__ == '__main__':
	main()
		