from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length != self.capacity:
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        while len(list_buffer_contents) != self.storage.length:
            self.current = self.storage.tail.value
            list_buffer_contents.append(self.current)
            self.storage.remove_from_tail()
            self.storage.add_to_head(self.current)
        return list_buffer_contents

        # if self.current is None:
        #     return
        # else:
        #     while len(list_buffer_contents) != self.storage.length:
        #             list_buffer_contents.append(self.current)
        #             self.storage.remove_from_tail()
        #             self.current = self.storage.head.value
        #             list_buffer_contents.append(self.current)
        #             self.storage.remove_from_head()

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
