# **Improved Merge Sort**

The improved merge sort method enhances the traditional merge sort by incorporating insertion sort for small subarrays.

- Divides the list into halves until sublists are smaller than a defined threshold.
- Each sublist is sorted using Insertion Sort.
- Merges the sorted sublists back together.

This hybrid approach leverages the efficiency of insertion sort on small datasets, resulting in better overall performance compared to standard merge sort, especially for practical input sizes.


**Example:**
```python
A = [2, 4, 1, 5, 3]
improved_merge_sort(A, k=3)
print(A)
# Output: [1, 2, 3, 4, 5]
```

## **Time Complexity**

$O(nk + n \lg (n/k))$

---

© 2025 Byron Velasco