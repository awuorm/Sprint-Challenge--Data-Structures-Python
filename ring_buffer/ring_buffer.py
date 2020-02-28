from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length != self.capacity:
            self.storage.add_to_tail(item)
        else:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        while len(list_buffer_contents) != self.storage.length:
            print(self.storage.head.value)
            self.current = self.storage.head.value
            list_buffer_contents.append(self.current)
            self.storage.remove_from_head()
            self.storage.add_to_tail(self.current)
        return list_buffer_contents


ring  = RingBuffer(4)
ring.append("a")
ring.append("b")
ring.append("c")
ring.append("d")
print(ring.get())
ring.append("e")
ring.append("f")
ring.append("g")
print(ring.get())
ring.append("h")
print(ring.get())
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
