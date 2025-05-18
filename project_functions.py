from math import inf


def partition(A, p, r):
	pivot = A[r]  # Choose the last element as the pivot
	i = p - 1  # Initialize the index for the smaller element
	for j in range(p, r):
		if A[j] <= pivot:  # If the current element is less than or equal to the pivot
			i += 1  # Increment the index for the smaller element
			A[i], A[j] = A[j], A[i]  # Swap the elements
	A[i + 1], A[r] = A[r], A[i + 1]  # Place the pivot in its correct position
	return i + 1  # Return the index of the pivot


def quick_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
			r = len(A) - 1

	def recursive_quick_sort(A, p, r):
		if p < r:  # Base case: stop when the sublist has one or no elements
			pivot_index = partition(A, p, r)  # Partition the list and get the pivot index
			recursive_quick_sort(A, p, pivot_index - 1)  # Recursively sort the left partition
			recursive_quick_sort(A, pivot_index + 1, r)  # Recursively sort the right partition

	# Call the inner recursive function
	recursive_quick_sort(A, p, r)


def merge_sort(A):
	# If the list has more than one element, proceed to sort
	if len(A) > 1:
		half = len(A) // 2  # Find the midpoint to divide the array
		left = A[:half]     # Create left subarray
		right = A[half:]    # Create right subarray

		# Recursively sort both halves
		merge_sort(left)
		merge_sort(right)

		# Append infinity to both subarrays to act as sentinels
		left.append(inf)
		right.append(inf)

		i = j = 0  # Initialize pointers for left and right subarrays

		# Merge the sorted subarrays back into A
		for k in range(len(A)):
			if left[i] <= right[j]:
				A[k] = left[i]  # Take from left if smaller or equal
				i += 1
			else:
				A[k] = right[j]  # Take from right otherwise
				j += 1
				

def insertion_sort(A):
	n = len(A)  # Get the length of the array
	for i in range(1, n):  # Iterate from the second element to the end
		key = A[i]         # Store the current element to be positioned
		j = i - 1          # Start comparing with the previous element
		# Shift elements of A[0..i-1], that are greater than key, to one position ahead
		while j >= 0 and key < A[j]:
			A[j + 1] = A[j]  # Move element one position to the right
			j -= 1           # Move to the previous element
		A[j + 1] = key       # Place the key after the last shifted element
		

def improved_merge_sort(A, k=16):
	# If the subarray size is less than or equal to k=16 (default), use insertion sort for efficiency
	if len(A) <= k:
		insertion_sort(A)
		return
	half = len(A) // 2        # Find the midpoint to divide the array
	left = A[:half]           # Create left subarray
	right = A[half:]          # Create right subarray
	# Recursively sort both halves using improved_merge_sort
	improved_merge_sort(left, k)
	improved_merge_sort(right, k)
	# Append infinity to both subarrays to act as sentinels
	left.append(inf)
	right.append(inf)
	i = j = 0                 # Initialize pointers for left and right subarrays
	# Merge the sorted subarrays back into A
	for k in range(len(A)):
		if left[i] <= right[j]:
			A[k] = left[i]    # Take from left if smaller or equal
			i += 1
		else:
			A[k] = right[j]   # Take from right otherwise
			j += 1