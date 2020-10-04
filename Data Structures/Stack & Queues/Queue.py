class Queue(object):
    def __init__(self):
        self.items = []

    def Enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def Size(self):
        return len(self.items)


q = Queue()
q.Enqueue(1)
q.dequeue()
print(q.Size())
print(q.isEmpty())
