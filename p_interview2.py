# Adam Rosenberg
# min max stack
# push() pop() peek()

# min(), max(), mean()

# optimize for run time, not space

# stack is LIFO, last in first out

class Plaid_Stack(object):



    def __init__(self):
        self.stack = []
        self.sorted_stack = []
        self.min = None
        self.max = None
        self.sum = 0
        self.number_of_elements = 0

    def push(self, element):

        if self.max == None:
            self.max = element

        if self.min == None:
            self.min = element

        if element > self.max:
            self.max = element

        if self.min != None and element < self.min:
            self.min = element

        self.stack.append(element)

        self.sorted_stack.append(element)
        self.sorted_stack.sort()

        self.sum += element
        self.number_of_elements += 1

    def pop(self):

        # want to make sure we're not popping
        # an empty stack TODO

        element_to_pop = self.stack.pop()

        self.sorted_stack.remove(element_to_pop)

        if element_to_pop == self.min:
            self.min = self.sorted_stack[0]

        if element_to_pop == self.max:
            self.max = self.sorted_stack[-1]

        self.sum -= element_to_pop
        self.number_of_elements -= 1

    def peek(self):
        return self.stack[0] if len(self.stack) > 0 else None

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_mean(self):
        return float(self.sum) / float(self.number_of_elements)

    def print_stack(self):
        print "\nprinting stack: "
        for element in self.stack:
            print element


stack = Plaid_Stack()
stack.push(1)
stack.push(3)
stack.push(5)
print stack.get_min(), stack.get_max()
stack.pop()
print stack.get_min(), stack.get_max()
stack.push(0)
print stack.get_min(), stack.get_max()
stack.print_stack()
print stack.get_mean()




# push(1), push(5), push(3), pop()
# each step check min and max

# push (1)
# min : 1, max: 1, sum: 1
# 1
# 1

# push(5)
# min : 1, max: 5, sum: 6
# 1, 5
# list: 1, 5

# push(3)
# min: 1, max: 5, sum: 9
# 1, 5, 3
# list: 1, 3, 5

# pop()
# min: 1, max: 5, sum: 6
# stack: 1, 5
# list: 1, 5

# pop()
# min: 1, max: 1, sum: 1
# 1 ... ... ...

# push(7), push(9)

