class Queue(object):
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        self.item.pop()

    def size(self):
        return len(self.item)

    def showQueue(self):
        return self.item


q = Queue()
q.enqueue("hello")
q.enqueue("world")
q.enqueue("there")
print(q.size())
q.dequeue()
print(q.size())
print(q.showQueue())
q.dequeue()
print(q.size())
print(q.showQueue())