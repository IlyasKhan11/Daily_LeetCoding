class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def Lview(self, root, level):
        if root is None:
            return
        
        # If this is the first node of this level
        if level == len(self.ans):
            self.ans.append(root.data)
        
        # Recur for left and right subtrees
        self.Lview(root.left, level + 1)
        self.Lview(root.right, level + 1)
    
    def leftView(self, root):
        self.ans = []
        self.Lview(root, 0)
        return self.ans

# Utility function to create a new tree node
def newNode(val):
    return Node(val)

# Function to build tree from input
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    # Create root of the tree
    root = Node(int(s[0]))
    queue = [root]
    i = 1
    
    # Level order construction
    while queue and i < len(s):
        currNode = queue.pop(0)
        
        # Left child
        if s[i] != "N":
            currNode.left = Node(int(s[i]))
            queue.append(currNode.left)
        i += 1
        
        # Right child
        if i < len(s) and s[i] != "N":
            currNode.right = Node(int(s[i]))
            queue.append(currNode.right)
        i += 1
    
    return root

# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip().split()
        root = buildTree(s)
        ob = Solution()
        result = ob.leftView(root)
        print(" ".join(map(str, result)))
