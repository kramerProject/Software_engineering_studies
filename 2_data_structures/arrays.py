import sys

class Array():
    def __init__(self, numbers):
        self.data = numbers

    def size(self):
        return len(size)

    def capacity(self):
        return sys.getsizeof(self.data)

    def is_empty(self):
        return not self.data

    def at(self, index):
        try:
            return self.data[index]
        except IndexError:
            return f"Index should be less or equal {len(self.data)-1}"
        

    def push(self, number):
        return self.data.append(number)

    def insert(self, index, number):
        first_part = self.data[:index]
        second_part = self.data[index:]
        first_part.append(number)
        self.data = first_part + second_part
        return self.data

    def pop(self):
        self.data.pop()

    def delete(self, item):
        del self.data[item]

    def remove(self, number):
        for index in range(0, len(self.data)):
            if index > len(self.data) - 1:
                return "Done"
            if self.data[index] == number:
                self.delete(index)

    def find(self, number):
        return self.data.index_of(10)

    def resize(self):
        pass

    def space(self):
        pass


numbers = [2,4,5,8,9,10]
my_array = Array(numbers)

print(my_array.at(20))
my_array.insert(2,40)
my_array.remove(40)


