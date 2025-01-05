"""
Missing element : Consider an array of non-negative integers. A second array is formed by shuffling the elements
of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
"""

def finder(arr1, arr2):
    sum = 0
    for element in arr1:
        sum+=element

    sum2 = 0
    for element in arr2:
        sum2+=element

    missing_element=sum - sum2

    print(missing_element)

finder([1,2,3,4,5],[5,2,3,4])