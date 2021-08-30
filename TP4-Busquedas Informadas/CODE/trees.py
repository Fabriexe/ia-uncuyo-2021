class Tree:
    root=None
    def __init__(self,value):
        Node=TreeNode(value)
        self.root=Node
class TreeNode:
    parent=None
    children=[]
    value=None

    def __init__(self,value,parent=None):
        self.value=value
        self.parent=parent
    
    def child(self,val):
        Node=TreeNode(val,self)
        self.children.append(Node)
        Node.parent=self
    

        
        
