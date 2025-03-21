
# Question: Find the Maximum Sum of a Subarray of Size in a given array
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"  # Edge case

    # Compute the sum of the first window
    max_sum = sum(arr[:k])
    window_sum = max_sum

    # Slide the window over the array
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # Add next element, remove first element of the window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example Usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of subarray of size", k, ":", max_sum_subarray(arr, k))