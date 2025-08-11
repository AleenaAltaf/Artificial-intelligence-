""" from collections import deque

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node , end=" ")
            visited.add(node)
            for neighbour in graph[node]:  # Fix here
                if neighbour not in visited:
                    queue.append(neighbour)

graph ={
    '0' : ['4','1'], 
    '1' : ['4','2','3','4'], 
    '2' : ['1','3'], 
    '3' : ['1','2','4'], 
    '4' : ['0','1','3']
}

BFS(graph, '0') 
from collections import deque

# Class for Graph
class Graph:
    def _init_(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]  # List of lists for adjacency

    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v's list

    def BFS(self, s):
        visited = [False] * self.V  # Mark all vertices as not visited
        queue = deque([s])  # Create a queue and enqueue the start vertex
        visited[s] = True  # Mark the starting vertex as visited

        while queue:
            s = queue.popleft()  # Dequeue a vertex
            print(s, end=" ")

            # Enqueue all adjacent vertices of s that haven't been visited
            for i in self.adj[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


g = Graph(4)  # Create a graph with 4 vertices (0 to 3)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2):")
g.BFS(2) 
from collections import deque
class BFS:
    def __init__(self,V):
        self.V=V
        self.adj=[[] for _ in range(V)]
    def add_v(self,v,w):
        self.adj[v].append(w)
    def bfs(self,s):
        visited = [False] * self.V
        Queue = deque([s])
        visited[s]=True
        while Queue:
            node = Queue.popleft()
            print (node , end=" ")
            for i in self.adj[node]:
                if not visited[i]:
                    Queue.append(i)
                    visited[i]= True
g = BFS(4)  # Create a graph with 4 vertices (0 to 3)

g.add_v(0, 1)
g.add_v(0, 2)
g.add_v(1, 2)
g.add_v(2, 0)
g.add_v(2, 3)
g.add_v(3, 3)

print("Following is Breadth First Traversal (starting from vertex 0):")
g.bfs(0)                    
        
        """
from collections import deque

# Class for Graph
class Graph:
    def __init__(self):
        self.adj = {}  # Dictionary for adjacency list

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def BFS(self, start, goal):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(f"Visiting: {node}")

            if node == goal:
                print(f"Goal {goal} found!")
                return

            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Create the graph
g = Graph()

# Add the edges (based on your tree)
g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')
g.addEdge('B', 'K')
g.addEdge('B', 'J')
g.addEdge('D', 'G')
g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')
g.addEdge('K', 'N')
g.addEdge('K', 'M')
g.addEdge('I', 'L')

# Perform BFS starting from 'A' and stop at 'G'
print("Breadth First Traversal (starting from A):")
g.BFS('A', 'G') 
"""class PriorityQueue:
    def _init_(self):
        self.list = []

    def enqueue(self, item, priority):
        # Add the item as a tuple (priority, item)
        self.list.append((priority, item))
        # Sort the list based on priority without using lambda
        self.list.sort(key=self.get_priority)

    def get_priority(self, item):
        # Extract the priority from the tuple
        return item[0]

    def dequeue(self):
        # Remove and return the item with the highest priority (lowest number)
        if self.list:
            return self.list.pop(0)[1]  # Return only the item, not the priority
        else:
            raise IndexError("Dequeue from an empty priority queue")
        

# Create an instance of PriorityQueue
pq = PriorityQueue()
# Enqueue items with their priorities
pq.enqueue(10, 2)  # Item 10 with priority 2
pq.enqueue(20, 1)  # Item 20 with priority 1
pq.enqueue(30, 3)  # Item 30 with priority 3

# Dequeue to get the item with the highest priority
print(pq.dequeue())  # Should print 20 (highest priority)"""