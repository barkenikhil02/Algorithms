class Deque(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def RearEnqueue(self, item):
        self.item.insert(0, item)

    def FrontEnqueue(self, item):
        self.item.append(item)

    def FrontDequeue(self):
        self.item.pop()

    def RearDequeue(self):
        self.item.pop(0)

    def Size(self):
        return len(self.item)


d = Deque()
