class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if (not stack.isEmpty()):
            return self.stack[-1]

    def print(self):
        print("---------Printing Stack------------")
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])
        print("")


if(__name__ == "__main__"):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.print()

    print("Pop function: ", stack.pop())

    print("Peek function: ", stack.peek())

    stack.print()
