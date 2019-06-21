#Python program to print topological sorting of a DAG 
from collections import defaultdict 

#Class to represent a graph 
# https://www.geeksforgeeks.org/topological-sorting/
class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #No. of vertices 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		# Call the recursive helper function to store Topological 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of the stack 
		print (stack)


# total number of nodes in the graph
'''
g= Graph(4)
g.addEdge('Server0', 'Server2'); 
g.addEdge('Server2', 'Server1'); 
g.addEdge('Server3', 'Server1'); 
'''
g= Graph(4)
g.addEdge(0, 2); 
g.addEdge(2, 1); 
g.addEdge(3, 1);

''' g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
'''
''' g= Graph(8) 
g.addEdge(2, 0); 
g.addEdge(2, 1); 
g.addEdge(2, 3); 
g.addEdge(1, 3); 
g.addEdge(5, 6); 
g.addEdge(5, 4); 
g.addEdge(6, 4); 
g.addEdge(7, 0); 
g.addEdge(8, 0); 
g.addEdge(5, 0); '''

print("Following is a Topological Sort of the given graph")
g.topologicalSort() 
#This code is contributed by Neelam Yadav   
