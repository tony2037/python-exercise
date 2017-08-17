
class Node:
    def __init__(self,value,leftNode=None,rightNode=None,layout=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.layout = layout
    def searching(self,key):
        if(self.value == key):
            print("Found %s at layout : %s" %(key,self.layout))
            return True
        if(self.leftNode != None):
            self.leftNode.searching(key)
        if(self.rightNode != None):
            self.rightNode.searching(key)
        return False

    def addNode(self,value,direction):
        if(direction == 'right' or direction == 'r'):
            #writed here
            print("do add right")
        if(direction == 'left' or direction == 'l'):
            #
            print("do add left")
    def deleteNode(self):
        print("")

    def printTree(self):
        if(self.value != None):
            print(self.value)
        if(self.leftNode != None):
            print('left|')
            self.leftNode.printTree()
        if(self.rightNode != None):
            print('right|')
            self.rightNode.printTree()
