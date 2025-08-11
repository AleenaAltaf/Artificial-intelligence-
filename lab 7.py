#task (a)
"""class Tree:
    def __init__(self):
        self.tree = {}

    def add_edge(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DLS(self, node, goal, limit, depth=0):
        if depth > limit:
            return False
        
        print(node, end=" ")

        if node == goal:
            print("\nGoal node found!")
            return True

        for child in self.tree.get(node, []):#agar node dictionary mein maujood hai,us ke children return karo.Agar nahi hai, toh khaali list [] return kar do — taake loop crash na kare.
            #call the DLS function recursively for the child node — and go one level deeper (depth + 1).
            found = self.DLS(child, goal, limit, depth + 1)
            if found:
                return True

        return False  # If goal not found within this depth
tree = Tree()
# Add edges (same as your current code)
tree.add_edge('A', 'B')
tree.add_edge('A', 'F')
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

print("\n\nDLS (Depth = 1):")
if not tree.DLS('A', 'G', limit=1):
    print("\nGoal not found within depth 1")
    
print("\nDLS (Depth = 2):")
if not tree.DLS('A', 'G', limit=2):
    print("\nGoal not found within depth 2")

print("\n\nDLS (Depth = 3):")
if not tree.DLS('A', 'G', limit=3):
    print("\nGoal not found within depth 3")"""
    
#task (b)
class Tree:
    def __init__(self):
        self.tree = {}

    def add_edge(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DLS(self, node, goal, limit, depth=0):
        if depth > limit:
            return False

        print(node, end=" ")
        if node == goal:
            print("\nGoal node found!")
            return True

        for child in self.tree.get(node, []):
            found = self.DLS(child, goal, limit, depth + 1)
            if found:
                return True

        return False  # Goal not found in this path

    def IDS(self, root, goal, max_depth):
        for limit in range(max_depth + 1):#goes from 0-5 cuz max-depth is 5
            print(f"\nTrying depth limit: {limit}")
            if self.DLS(root, goal, limit):#calls the dls method
                print(f"\nGoal found at depth {limit}")
                return
        print("\nGoal not found within max depth.")

tree = Tree()
# Add edges
tree.add_edge('A', 'B')
tree.add_edge('A', 'F')
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

# Call IDS
print("\n\nIDS (Max Depth = 5):")
tree.IDS('A', 'G', max_depth=5)
