def QuickSort(i, j, k):
    if i < j:
        k = Partition(i, j, k)
        QuickSort(i, k - 1, k)
        QuickSort(k + 1, j, k)
def Partition(start, end, pivot):
    pivot = start
    for i in range(start + 1, end + 1):
        if A[i] < A[pivot]:
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]
    A[start], A[pivot] = A[pivot], A[start]
    return pivot

A = [5, 4, 3, 2, 1]

QuickSort(0, len(A) - 1, 0)
print(A)