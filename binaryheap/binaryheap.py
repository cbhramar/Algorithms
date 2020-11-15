import math

class Heap():
	def __init__(self, type):
		self.heap = []
		if type == 'MIN':
			self.op = 'MIN'
			self.identity = -math.inf
		else:
			self.op = 'MAX'
			self.identity = math.inf

	def operator(self, element1, element2):
		if self.op == 'MIN':
			return element1 > element2
		else:
			return element1 < element2

	def parent(self, index):
		return (index-1)//2

	def left(self, index):
		return 2*index + 1

	def right(self, index):
		return 2*index + 2

	def swap(self, index1, index2):
		self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

	def head(self):
		return self.heap[0]

	def extract(self):
		return self.heap.pop(0)

	def update(self, index, newelement):
		self.heap[index] = newelement
		while index != 0 and self.operator(self.heap[self.parent(index)], self.heap[index]):
			self.swap(index, self.parent(index))
			index = self.parent(index)

	def insert(self, element):
		self.heap.append(element)
		index = len(self.heap)-1
		while index!=0 and self.operator(self.heap[self.parent(index)], self.heap[index]):
			self.swap(index, self.parent(index))
			index = self.parent(index)

	def delete(index):
		update(index, self.identity)
		extract()

	def print(self):
		print(self.heap)

def main():
	heap = Heap('MAX')
	heap.insert(1)
	print(heap.head())
	heap.insert(2)
	heap.print()
	print(heap.extract())
	heap.insert(-1)
	heap.insert(0)
	heap.insert(3)
	heap.insert(1)
	heap.insert(13)
	heap.print()
	print(heap.extract())
	heap.insert(1)
	heap.print()

if __name__ == '__main__':
	main()
