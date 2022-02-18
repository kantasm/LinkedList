## 1-->2-->3

class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_list(self):
        if self.head is None:
            print('Linked list is empty')
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Error: Invalid index")

        if index==0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, index,data ):
        if index<0 or index>=self.get_length():
            raise Exception("Error: Invalid index")

        if index==0:
            self.insert_at_begin(data)
            return

        count=0
        itr=self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def get_index(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return count
            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        index = self.get_index(value)
        self.remove_at(index)

    def insert_after_value(self,curr_value, new_value):
        index = self.get_index(curr_value) + 1
        self.insert_at(index, new_value)

    def insert_before_value(self,curr_value, new_value):
        index = self.get_index(curr_value)
        self.insert_at(index, new_value)

    #insert_after_value
    #remove_by_value

if __name__ == '__main__':
    ll = LinkedList()
    #ll.insert_at_begin(1)
    #ll.insert_at_begin(2)
    #ll.insert_at_begin(3)
    #ll.insert_at_end(0)
    #ll.insert_at_end(4)
    ll.insert_values(['Mango','Bannana','Apple','Grapes','Orange'])
    ll.print_list()
    #print(ll.get_length())
    ll.remove_at(3)
    ll.print_list()
    ll.insert_at(0,"Figs")
    ll.print_list()
    print(ll.get_index("Bannana"))
    ll.remove_by_value("Apple")
    ll.print_list()
    ll.insert_after_value("Bannana","Grapes")
    ll.print_list()
    ll.insert_before_value("Bannana", "Raspberry")
    ll.print_list()
    pass
