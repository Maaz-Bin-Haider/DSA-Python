# Prefix Sum is the sum of all elements from index 0 to i
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


arr = ['a','b','c','d']
print("Original Array:", arr)
print("Prefix Sum Array:", prefix_sum(arr))