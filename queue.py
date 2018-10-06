class Queue:

    def __init__(self):
        self.items = []

    def eqneueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.eqneueue(4)