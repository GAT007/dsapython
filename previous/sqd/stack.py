class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return 'Inserted'

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()

print(s.isEmpty())

print(s.push(1))
print(s.push('two'))

print(s.peek())

print(s.size())

print(s.pop())
print(s.pop())

    #Stack() returns empty stack
    #push returns
