class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0
        
def level(root):
    m={}
    q=[(root,0)]
    while q:
        node,lvl=q.pop(0)
        if lvl not in m:
            m[lvl]=[]
        m[lvl].append(node.data)
        if node.left:
            q.append((node.left,lvl+1))
        if node.right:
            q.append((node.right,lvl+1))
    print("Level Order Traversal: ")
    for lvl in m:
        print(m[lvl])
             
        
root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
root.right.right=Node("G")
level(root)
