import Node

n3=Node.Node(2,None,None,2)
n2=Node.Node(3,None,None,2)
n1=Node.Node(1,n2,n3,1)

n1.printTree()
n1.searching(2)
