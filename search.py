class Directed_Graph(object):
	
	def __init__(self, AdjacencyDict):
		self.graph = AdjacencyDict
		self.NumVert = len(self.graph)
		self.NumEdge = sum([len(self.graph[k]) for k in self.graph])
		
	def AddEdge(self, v, w):
		self.graph[v].append(w)
	
	def IterPointingTo(self, vertex):
		for vert in self.graph[vertex]:
			yield vert
	
	def Reverse(self):
		revgraph =  {x:[] for x in self.graph}
		
		for u in self.graph:
			for v in self.graph[u]:
				revgraph[v].append(u)		
		
		return revgraph
	
	def ToString(self):
		for i in self.graph:
			print(i,self.graph[i])
		print("Verticies:", self.NumVert)
		print("Edges:", self.NumEdge)

def Depth_First_Search(Graph, StartVertex, Explored):
	Explored[StartVertex-1] = True
	
	for Vertex in Graph.IterPointingTo(StartVertex):
		if not Explored[Vertex-1]:
			yield(Vertex)
			yield from Depth_First_Search(Graph, Vertex, Explored)
					
if __name__ == "__main__":
	g = {1:[2,3],2:[4,5,6],3:[1,6],4:[1,2,3,4],5:[1,2],6:[6]}
	G = Directed_Graph(g)
	StartVertex = 1
	Explored = [False] * G.NumVert
	
	G.ToString()
	
	print(StartVertex)
	for i in Depth_First_Search(G, StartVertex, Explored):
		print(i)