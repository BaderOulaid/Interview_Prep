class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def to_string(self):
        for item in self.items:
            print item


test_stack = Stack()

test_stack.push(4)
test_stack.push(2)
test_stack.pop()
# print test_stack.peek()
test_stack.to_string()

