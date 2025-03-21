
# Question: Find Pair Which sum up to target in a Sorted Array
def two_pointer_sum(arr, target):
    left, right = 0, len(arr) - 1  # Two pointers

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right]) 
        elif current_sum < target:
            left += 1  
        else:
            right -= 1 

    return None  


arr = [1, 2, 3, 4, 6, 8, 10]
target = 10
print("Pair with sum", target, ":", two_pointer_sum(arr, target))