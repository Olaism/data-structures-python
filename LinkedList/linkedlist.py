from node import Node


class LinkedList:
    """ A representation of linked list data structure """

    def __init__(self):
        self.head = None

    def show(self):
        """ Show the data in the linked list """

        if not self.head:
            return []
        else:
            values = []
            n = self.head
            while n is not None:
                values.append(n.data)
                n = n.ref
            return values

    def add_left(self, data):
        """ Add a node at the the beginning of the list """
        new_node = Node(data)  # create a new node
        new_node.ref = self.head  # The new node refrence to the head of the list
        self.head = new_node  # The new node is made the head of the list
