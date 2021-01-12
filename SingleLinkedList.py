
class SingleLinkedListNode(object):
    """docstring for SingleLinkedListNode."""

    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.value

    def set_next(self, next_node):
        self.next = next_node

    def set_value(self, new_value):
        self.value = new_value

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):
    """docstring for SingleLinkedList."""

    def __init__(self):
        self.startNode = SingleLinkedListNode()
        self.endNode = SingleLinkedListNode()
        self.count = 0

    def get_number_of_items(self):
        return self.count

    def push(self, data):
        """Appends a new value at the end of the linked list"""

        newNode = SingleLinkedListNode(data)
        if self.startNode.next == None:
            self.startNode.set_next(newNode)
            self.endNode.set_next(newNode)
        else:
            current_node = self.startNode
            while current_node.next != None:
                current_node = current_node.next

            current_node.set_next(newNode)
            self.endNode.set_next(newNode)

        self.count = self.count + 1

    def get_first_item(self):
        return self.startNode.next

    def get_last_item(self):
        return self.endNode.next

    def get_node_at_index(self, index):
        """ Return the node from the given index"""

        if index > self.count:
            return self.startNode
        else:
            current_node = self.startNode
            iteration = 0
            while iteration != index:
                current_node = current_node.next
                iteration = iteration + 1
                
            return current_node
