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
            print(current_value)
        current_value.next = last_value
        self.__length += 1



linked.insert_first(40)
linked.insert_first(20)
linked.insert_first(22)
linked.insert_first(12)
linked.insert_last(23)
print(linked)