# **Improved Merge Sort**

This module contains `ImprovedMergeSort.ipynb` which implements the improved Merge Sort algorithm.

## **Function:** `InsertionSort(A)`

For a detailed study, refer to my other project: [Sorting Algorithms](https://github.com/ByronVelasco/SortingAlgorithms).

## **Function:** `ImprovedMergeSort(A, k_threshold = 16)`

## **Improved Merge Sort**

- Divides the list into halves until sublists are smaller than a defined threshold.
- Each sublist is sorted using Insertion Sort.
- Merges the sorted sublists back together.

**Note:**  
The default threshold `k_threshold = 16` was selected because it yielded better results on my personal computer. Feel free to experiment with different values to find the most optimal one for your system.


**Example:**
```python
A = [2, 4, 1, 5, 3]
ImprovedMergeSort(A, 3)
print(A)
# Output: [1, 2, 3, 4, 5]
```

## **Time Complexity**

$O(nk + n \lg (n/k))$

---

© 2025 Byron Velasco