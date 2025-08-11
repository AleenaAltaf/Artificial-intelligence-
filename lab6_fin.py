#task1
"""class Tree:
    def __init__(self, size):
        self.tree = [[] for _ in range(size)] # creating adjacenecy list ,list of list [[],[],...]

    def add_edge(self, parent, child):
        # Add parent and child to the tree if they don't exist
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DFS(self, root):
        stack = [root]
        visited = set()#creating empty set to maintain record for visited nodes...

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                # Add children to the stack in reverse order for correct DFS order,1st right then left
                stack.extend(reversed(self.tree[node]))

# Create the tree
tree = Tree(13) #0-12 room for 12 nodes 
tree.add_edge(1,2) #[[2],[],,,]
tree.add_edge(1,7) #[[2,7],[],,,]
tree.add_edge(1,8) #[[2,7,8],[],,,] and so on
tree.add_edge(2,3)
tree.add_edge(2,6)
tree.add_edge(3,4)
tree.add_edge(3,5)
tree.add_edge(8,9)
tree.add_edge(8,12)
tree.add_edge(9,10)
tree.add_edge(9,11)






print("\nDFS traversal of the tree starting from node 0:")
tree.DFS(1)"""
#task2
class Tree:
    def _init_(self):
        self.tree = {}#creating dictionary here

    def add_edge(self, parent, child):
        # Add parent and child to the tree if they don't exist
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DFS(self, root, goal):
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                # Check if the current node is the goal node
                if node == goal:
                    print("\nGoal node found!")
                    return

                # Add children to the stack in reverse order for correct DFS order
                stack.extend(reversed(self.tree[node]))

        print("\nGoal node not found.")

# Create the tree
tree = Tree()
tree.add_edge('A', 'B')#{ A:["B"]}
tree.add_edge('A', 'F')#{ A:["B","F"] and so on}
tree.add_edge('A', 'D')
tree.add_edge('A', 'E')
tree.add_edge('B', 'K')
tree.add_edge('B', 'J')
tree.add_edge('K', 'N')
tree.add_edge('K', 'M')
tree.add_edge('D', 'G')
tree.add_edge('E', 'C')
tree.add_edge('E', 'H')
tree.add_edge('E', 'I')
tree.add_edge('I', 'L')

# Perform DFS with character nodes
start_node = 'A'
goal_node = 'G'
print(f"\nDFS traversal of the tree starting from node {start_node} to find {goal_node}:")
tree.DFS(start_node, goal_node)

