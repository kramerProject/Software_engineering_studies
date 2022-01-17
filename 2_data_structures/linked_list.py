from node import ListNode

class LinkedList:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self.head_value})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        first_value = ListNode(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def insert_last(self, value):
        last_value = ListNode(value)
        current_value = self.head_value

        if current_value is None:
            return self.insert_first(value)

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1

    def empty(self):
        return self.__length == 0

    def value_at(self, index):
        if index > self.__length - 1:
            return f"Index should be less or equal {self.__length - 1}"
        
        counter = 0
        result = self.head_value
        while counter != index:
            result = result.next
            counter += 1
        return result.value

    def pop_front(self):
        result = self.head_value
        self.head_value = result.next
        self.__length -= 1
        return f"First value {result.value} removed from head"

    def pop_back(self):
        previous = None
        next = self.head_value.next
        while next.next:
            previous = next
            next = next.next
            print(next)
        popped =  next.value
        next = previous
        next.next = None
        self.__length -= 1
        return popped
    
    def front(self):
        return self.value_at(0)

    def back(self):
        return self.value_at(self.__length - 1)



linked = LinkedList()
linked.insert_first(40)
linked.insert_first(20)
linked.insert_first(22)
linked.insert_first(12)
linked.insert_last(23)
print(linked.pop_back())
print(linked.back())
print(linked)
