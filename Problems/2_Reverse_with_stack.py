#Creating Sinlge linked list and Adding data to it
#And displaying the Linked list

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty..!")
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=" ")
                temp = temp.next

    def reverse_order(self):
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next

        while stack:
            print(stack.pop(),"-->",end=" ")

#Creating obeject for Linked List
l = SingleLinkedList()

#Creating a nodes and Adding data to it
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Connecting the Nodes using the references(next)
l.head= n1
n1.next = n2
n2.next = n3
n3.next = n4

#Displaying the Linked List
l.display()
print()
l.reverse_order()
