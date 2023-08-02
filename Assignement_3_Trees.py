# Q1. Implement Binary tree--

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PreorderTraversal(root))

#------------------------------------------------------------------------------------------------

#Q2. Find height of a given tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
    if root is None:
        # If TRUE return 0
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
    
    return max(leftAns, rightAns) + 1
 
# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " + str(height(root)))

#----------------------------------------------------------------------------------------------------

#Q3. Perform Pre-order, Post-order, In-order traversal

#IN ORDER
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

def inorderTraversalUtil(root, answer):

    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.val)
    inorderTraversalUtil(root.right, answer)
    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorderTraversal(root))


#PRE-ORDER--
class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def preorderTraversal(root):
    answer = []

    preorderTraversalUtil(root, answer)
    return answer

def preorderTraversalUtil(root, answer):

    if root is None:
        return 

    answer.append(root.val)

    preorderTraversalUtil(root.left, answer)
    preorderTraversalUtil(root.right, answer)
    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorderTraversal(root))

#Post-Order--

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorderTraversal(root):
    answer = []

    postorderTraversalUtil(root, answer)
    return answer

def postorderTraversalUtil(root, answer):

    if root is None:
        return

    postorderTraversalUtil(root.left, answer)

    postorderTraversalUtil(root.right, answer)

    answer.append(root.val)

    return
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorderTraversal(root))
#---------------------------------------------------------------------------------------------------

#Q4. Function to print all the leaves in a given binary tree--

class newNode:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to print leaf
# nodes from right to left
def printLeafNodes(root):
     
    # If node is null, return
    if root == None:
        return
     
    # If node is leaf node,
    # print its data
    if (root.left == None and
        root.right == None):
        print(root.data, end = " ")
        return
     
    if root.right:
        printLeafNodes(root.right)
     
    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8)
root.right.right.left = newNode(9)
root.left.left.left.right = newNode(10)
 
printLeafNodes(root)
#-----------------------------------------------------------------------------------------------------

#Q5. Implement BFS (Breath First Search) and DFS (Depth First Search)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling

#--------------------------------------------------------------------------------------------------

#Q6. class Node:
    # Constructor to create a new Node
def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
 
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
def leftLeavesSum(root):
    res = 0
    if root is not None:
        if isLeaf(root.left):
            res += root.left.key
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)
 
        # Recur for right child of root and update res
        res += leftLeavesSum(root.right)
    return res
 
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)       
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))

#---------------------------------------------------------------------------------------------

# Q7. Find sum of all nodes of the given perfect binary tree

class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class SumOfNodes:  
    def __init__(self):  
        
        self.root = None;  
    def calculateSum(self, temp):  
        sum = sumRight = sumLeft = 0;  
          
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
        else:  
            if(temp.left != None):  
                sumLeft = self.calculateSum(temp.left);  
              
            #Calculate the sum of nodes present in right subtree  
            if(temp.right != None):  
                sumRight = self.calculateSum(temp.right);  
              
            sum = temp.data + sumLeft + sumRight;   
        return sum;  
   
bt = SumOfNodes();  
bt.root = Node(5);  
bt.root.left = Node(2);  
bt.root.right = Node(9);  
bt.root.left.left = Node(1);  
bt.root.right.left = Node(8);  
bt.root.right.right = Node(6);  
   
print("Sum of all nodes of binary tree: " + str(bt.calculateSum(bt.root)));  

#--------------------------------------------------------------------------------------------------

#Q8. Count subtress that sum up to a given value x in a binary tree

class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def countSubtreesWithSumX(root, count, x):
 
    if (not root):
        return 0
    ls = countSubtreesWithSumX(root.left,count, x)

def countSubtreesWithSumX(root, count, x):
 
    # if tree is empty
    if (not root):
        return 0
 
    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,count, x)
 
    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,count, x)
    Sum = ls + rs + root.data
 
    # if true
    if (Sum == x):
        count[0] += 1    

        return count[0]
    if __name__ == '__main__':
        root = getNode(5)
root.left = getNode(-10)
root.right = getNode(3)
root.left.left = getNode(9)
root.left.right = getNode(8)
root.right.left = getNode(-4)
root.right.right = getNode(7)
 
x = 7
print("Count =", countSubtreesWithSumX(root, x))

#----------------------------------------------------------------------------------------------------

#Q10. Print the nodes at odd levels of a tree:


class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def printOddLevelOddNodes(root):
    if (root == None):
        return
    q =[]
    q.append(root)
    evenLevel = True
    while (1):
         
        
        nodeCount = len(q)
        if (nodeCount == 0):
            break
        evenNodePosition = True
        while (nodeCount > 0):
            node = q[0]
            if not evenLevel and not evenNodePosition:
                print(node.data, end =" ")
            q.pop(0)
            if (node.left != None):
                q.append(node.left)
            if (node.right != None):
                q.append(node.right)
            nodeCount-= 1
            evenNodePosition = not evenNodePosition
         
        # Switch the even level flag
        evenLevel = not evenLevel

if __name__ == '__main__':
    root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.right.left = newNode(8)
root.left.right.right = newNode(9)
root.left.right.left.left = newNode(10)
root.left.right.right.right = newNode(11)
printOddLevelOddNodes(root)
                 
