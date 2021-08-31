class Node:
    def _init_(self,data):
        self.previous = None
        self.next = None
        self.list = data

class doubly_linked_list:
    def _init_(self):
        self.head = None

    def Insert_At_Start(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            new_node.next = None
            self.head  = new_node
            return
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            new_node.previous = None
            self.head = new_node
            return


    def Insert_At_End(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = None
            new_node.previous = None
            self.head = new_node
            return
        else:
            new_node = Node(data)
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node
            new_node.previous = n
            new_node.next = None
            return
    def Insert_At_Index(self,data,pos):
        n= Node(data)
        temp = self.head
        for i in range(1,pos-1):
                temp = temp.next
        if(temp.next == None):
            return self.Insert_At_End(data)
        else:
            n.previous = temp
            n.next = temp.next
            temp.next.previous = n
            temp.next = n
            return
    def delete_at_beginnning(self):
        temp = self.head
        if temp is None:
            print("The List is empty")
            return
        else:
            self.head = temp.next
            temp.next = None
            return

    def find_len(self):
        temp = self.head
        len = 0
        while temp is not None:
            len += 1
            temp = temp.next
        return len
    def delete_at_end(self):
        previous = self.head
        temp = self.head.next
        if previous is not None and temp is not None:
                while temp.next is not None:
                    temp = temp.next
                    previous = previous.next
                previous.next = None
                temp.previous = None
                return
        elif temp is None:
            return self.delete_at_beginnning()
        else:
            print('The list is empty')
            return        
    
    def delete_at_Index(self,pos):
        prev = self.head
        temp = self.head.next
        len_list = self.find_len()
        if len_list == 0:
            print("The list is empty")
            return
        elif len_list == 1 or pos == 1:
            return self.delete_at_beginnning()
        elif len_list == pos:
            return self.delete_at_end()
        else:
                for i in range(1,pos-1):
                        temp = temp.next
                        prev = prev.next
                prev.next = temp.next
                temp.next.previous = prev
                temp.next = None
                temp.previous = None
                return

    def display(self):
        n = self.head
        while n:
            print(f"{n.list}")
            n = n.next

new_doubly = doubly_linked_list()
new_doubly.Insert_At_End(39)
new_doubly.Insert_At_Start(4)
new_doubly.Insert_At_Start(5)
new_doubly.Insert_At_Start(7)
new_doubly.Insert_At_Start(3)
new_doubly.Insert_At_End(32)
new_doubly.Insert_At_Start(21)
new_doubly.Insert_At_Index(3,2)
new_doubly.delete_at_Index(1)
new_doubly.delete_at_Index(7)
new_doubly.display()