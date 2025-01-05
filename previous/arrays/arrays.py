import sys

my_list = [1,2,3]
my_tuple = (1,2,3)
my_string = '123'

#Set n
n = 10
data = []

for i in range(n):
    a = len(data)

    b = sys.getsizeof(data)

    print(f'Length {a} Size in bytes {b}')

    data.append(i)

