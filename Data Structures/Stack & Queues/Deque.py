class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def Size(self):
        return len(self.items)

    def seeAll(self):
        return self.items


d = Deque()
print(d.isEmpty())
d.addFront("hello")
d.addRear("World")
print(d.Size())
print(d.removeFront())
print(d.Size())
print(d.seeAll())
