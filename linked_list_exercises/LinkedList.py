# solution for 1st question, implement single linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

# solving question 2 find the size of the linked list
    def count(self):
        if self.head is None:
            return 0
        count =0
        inital = self.head

        while inital:
            inital = inital.next
            count+=1

        return count
    

myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.display()
print(myList.count())

