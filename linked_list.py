class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def printVal(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val)
            currentNode = currentNode.next
        
    def appendNode(self, node):
        if isinstance(node, Node):
            currentNode = self.head
            
            while currentNode:
                if currentNode.next is not None:
                    currentNode = currentNode.next
                else:
                    currentNode.next = node
                    break
        else:
            raise ValueError("Input data is not Node type.")

linkList = LinkedList()
linkList.head = node1
linkList.appendNode(node2)
linkList.appendNode(node3)

print(linkList.head.next.next.val)
linkList.printVal()