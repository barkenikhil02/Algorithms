class Stack(object):
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []


s = Stack()
print(s.isEmpty())
print(s.size())
s.push(4)
print(s.peek())
print(s.pop())
print(s.size(), "size is")
