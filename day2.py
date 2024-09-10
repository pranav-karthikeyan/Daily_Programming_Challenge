# Day 2 - Challenge 2
'''
Find the missing number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing Number : 3
'''

arr = [1, 2, 3, 4]
# Method 1: Find through iteration
for i in range(len(arr)):
    if arr[i] != i+1:
        print(i+1)     # Print the missing number if mismatch found
        break
else:
    # If the loop completes without finding a mismatch, then the missing number must be next one after the last element
    print(len(arr)+1)

#Method 2: Sum method
def missingNo(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2  # Sum of first n natural numbers
    actual = sum(arr)  # Sum of elements in the array
    missed = expected - actual  # The missing number
    return missed

print(missingNo(arr))