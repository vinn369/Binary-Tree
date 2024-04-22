class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0
        
def vertical(root):
    m={}
    q=[(root,0)]
    while q:
        node,hd=q.pop(0)
        if hd not in m:
            m[hd]=[]
        m[hd].append(node.data)
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
    print("Vertical Order Traversal: ")
    for hd in sorted(m):
        print(m[hd])
             
        
root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
root.right.right=Node("G")
vertical(root)
