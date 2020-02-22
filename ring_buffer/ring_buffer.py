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
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            
            if len(self.storage) == 1:
                self.current = self.storage.tail
        else:
            self.current.value = item
            self.current = self.current.next if self.current.next else self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [item for item in self if not None]

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
