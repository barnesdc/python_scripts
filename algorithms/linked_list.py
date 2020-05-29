""" Linked List

Steps:
1. Make a node class
2. Create the node
3. Operation
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0  # keeps track of number of nodes in list

    def get_count(self):
        return self.count

    def insert(self, data):
        # insert at head
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, data):
        item = self.head

        while item != None:
            if item.get_data() == data:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, index):
        if index > self.count - 1:
            return

        if index == 0:
            self.head = self.head.get_next()
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index - 1:
                node = node.get_next()
                tempIndex += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        temp_node = self.head
        while temp_node != None:
            print("Node: ", temp_node.get_data())
            temp_node = temp_node.get_next()


# create a linked list and insert some items

new_list = LinkedList()
new_list.insert(23)
new_list.insert(24)
new_list.insert(47)
new_list.insert(48)
new_list.insert(95)
new_list.insert(96)
new_list.dump_list()

print("Item count: ", new_list.get_count())
print("Finding item: ", new_list.find(24))
print("Finding item not in list: ", new_list.find(21))

new_list.deleteAt(5)
new_list.dump_list()
