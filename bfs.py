def bfs(graph, vertex):
	visited = [False]*len(graph)
	queue = []
	queue.append(vertex)
	visited[vertex] = True

	while queue:
		vertex = queue.pop(0)
		print(vertex, end = ' ')

		for i in graph[vertex]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True

	print()

if __name__ == '__main__':
	graph = dict()
	graph[0] = [0,3] 
	graph[1] = [2,4,5] 
	graph[2] = [2,3,4] 
	graph[3] = [3,1]
	graph[4] = [0,2]
	graph[5] = [5,3,1]

	bfs(graph, 2)
