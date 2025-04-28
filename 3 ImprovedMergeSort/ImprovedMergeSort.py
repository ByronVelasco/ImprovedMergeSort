# %% [markdown]
# ## **Imported Libraries**

# %%
from math import inf

# %% [markdown]
# ## **InsertionSort**

# %%
def InsertionSort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i-1
    while j >= 0 and key < A[j]:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

# %% [markdown]
# # **ImprovedMergeSort Algorithm**

# %%
def ImprovedMergeSort(A, k_threshold = 16):
  if len(A) <= k_threshold:
    InsertionSort(A)
    return
  half = len(A) // 2
  left = A[:half]
  right = A[half:]
  ImprovedMergeSort(left, k_threshold)
  ImprovedMergeSort(right, k_threshold)
  left.append(inf)
  right.append(inf)
  i = j = 0
  for k in range(len(A)):
    if left[i] <= right[j]:
      A[k] = left[i]
      i += 1
    else:
      A[k] = right[j]
      j += 1


