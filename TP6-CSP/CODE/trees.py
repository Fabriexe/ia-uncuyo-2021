class Tree:
    root=None
    def __init__(self,value):
        Node=TreeNode(value)
        self.root=Node
class TreeNode:
    parent=None
    height=None
    children=[]
    value=None

    def __init__(self,value,height=None,parent=None):
        self.value=value
        self.parent=parent
        self.height=height
    
    def child(self,val):
        Node=TreeNode(val,self)
        self.children.append(Node)
        Node.parent=self
    

        
        
