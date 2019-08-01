class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    # Method for inserting a new node at the start of a Linked List   
    def insert_at_front(self,data):
        new_node = Node()
        new_node.setData(data)
        
        if self.head is None:
            self.setHead(new_node)
        else:
            curr = self.head
            self.setHead(new_node)
            self.head.setNext(curr)
