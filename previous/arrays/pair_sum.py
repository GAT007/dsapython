#Given an integer array, output all the unique pairs that sum up to a specific value of k

def pair_sum(arr, k):
    #Edge case check
    if len(arr) < 2 :
        return

    #Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num,target)), max(num,target)))

    #return len(output)
    #This is just a high level print statement
    return '\n'.join(map(str, list(output)))


print(pair_sum([1,3,2,2], 4))

