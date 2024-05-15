import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.storage.length > 0:
            return self.storage.remove_from_tail()
            self.size -= 1
        # else:
        #     return 

    def len(self):
        return self.storage.__len__()

# test = Queue()
# print(test.len())
# test.enqueue(100)
# test.enqueue(101)
# test.enqueue(102)
# print(test.len())
