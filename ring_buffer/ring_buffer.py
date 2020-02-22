from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
    
    def __iter__(self):
        current = self.storage.head
        while current:
            item, current = current, current.next
            yield item.value

    def append(self, item):
        # not yet at capacity? append to tail
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            
            # initialize self.current when adding the first item to the list
            if len(self.storage) == 1:
                self.current = self.storage.tail
        else:
            # list is full, start overwritting the oldest element
            self.current.value = item
            # move current to the next oldest. loop back to the head upon reaching the tail
            self.current = self.current.next if self.current.next else self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [item for item in self if not None]

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------

# this just seems like a superior way to implement this structure?
# doing it with a linked list kinda sucked. A lot of overhead for seemingly no payoff

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current = self.current + 1 if self.current < len(self.storage) - 1 else 0

    def get(self):
        return [item for item in self.storage if item is not None]
