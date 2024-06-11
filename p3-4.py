class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
class BST:
    def addnode(self,root,data):
        newmode=node(data)
        if root==None:
            return newmode
        else:
            if data<root.data:
                if root.left  is None:
                    root.left=newmode
            else:
                self.addnode(self.root.left,data)
            
    def inorder(self,root):
        pass
    def postorder(self,root):
        pass
    def level_order(self,root):
        q=[root]
        while len(q)!=0:
            ele=q.pop(0)
            print(ele.data,end='')
            if ele.left!=None:
                q.append(ele.left)
            if ele.right!=None:
                q.append(ele.right)
    def          



