class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self,data):
        new_node = Node()
        new_node.setData(data)
        
        if self.head is None:
            self.head = new_node
        else:
            prev = None
            curr = self.head
            while curr is not None:
                prev = curr
                curr = curr.next
                
            prev.next = new_node
