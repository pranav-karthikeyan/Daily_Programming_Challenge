# Day 4 - Challenge 4
'''
You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input:
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output:
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
'''

def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def merge_arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    gap = next_gap(m + n)
    
    while gap > 0:
        i = 0
        # Compare elements in arr1
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
        # Compare arr1 and arr2 ele
        j = max(0, gap - m)
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        # Compare ele in arr2
        if j < n:
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        
        # Reduce gap
        gap = next_gap(gap)

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge_arrays(arr1, arr2)

print(f"{arr1} \n{arr2}")
