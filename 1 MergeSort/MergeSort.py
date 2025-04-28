# %% [markdown]
# ## **Additional Libraries**

# %%
from math import inf

# %% [markdown]
# ## **Merge Sort Algorithm**

# %%
def MergeSort(A):
  if len(A) > 1:
    half = len(A) // 2
    left = A[:half]
    right = A[half:]
    MergeSort(left)
    MergeSort(right)
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


