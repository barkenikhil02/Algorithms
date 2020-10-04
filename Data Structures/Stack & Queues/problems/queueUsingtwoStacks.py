class Queue2stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def showstack(self):
        return ("instack", self.instack, "outstack", self.outstack)


q2s = Queue2stacks()
q2s.enqueue('a')
q2s.enqueue('b')
q2s.enqueue('c')
q2s.dequeue()
print(q2s.showstack())
