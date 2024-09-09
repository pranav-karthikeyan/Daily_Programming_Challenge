#Day 2 - 03/09/2024
'''
You are given an unsorted array of integers. Your task is to find the median of the array. The median is the middle value in an ordered list of numbers. If the list has an even number of elements, the median is the average of the two middle numbers.

Implement a function that returns the median of the array without explicitly sorting the entire array.
Eg: Input = [3, 2, 1, 4, 5]
Output = 3

Eg 2: Input = [7, 10, 4, 3, 20, 15]
Output: 8.5
'''

def sort_array(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i, l):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]         # Make it in ascending order by swapping
    return arr

def find_median(arr):
    l = len(arr)
    if l%2 !=0:
        return arr[l//2]        # floor division to round of index
    res = arr[(l//2) - 1] + arr[l//2]
    return res/2

arr = [7, 10, 4, 3, 20, 15]
result = sort_array(arr)
print(result)
print(find_median(result))
