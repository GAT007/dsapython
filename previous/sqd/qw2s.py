#Implement a queue with 2 stacks

class QueueWith2Stacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        if len(self.stack2)!=0:
            while len(self.stack2)!=0:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(item)
        else:
            self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1)!=0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


q = QueueWith2Stacks()
q.enqueue('1')
q.enqueue('2')
q.enqueue('3')
print(q.dequeue())
