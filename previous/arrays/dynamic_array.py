class M(object):

    def public(self):
        print('Use tab to see me')

    def _private(self):
        print('You won\'t be able to tab to see me!')

import ctypes

class DynamicArray():

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        if not 0 <= idx < self.n:
            raise IndexError('Index out of range')
        else:
            return self.A[idx]

    def append(self, ele):
        if self.n == self.capacity or self.n>self.capacity:
            self.__resize__(2*self.capacity) #2x if capacity isn't enough

        self.A[self.n] = ele
        self.n += 1

    def __resize__(self, new_capacity):
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B

        self.capacity = new_capacity


    def make_array(self, new_capacity):
        return (new_capacity*ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr)
arr.append(3)
print(arr.capacity)
