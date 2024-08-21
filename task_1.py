def solution(A):
    if len(A) > 1000000000:
        return -1
    return mergesort(A, 0, len(A) - 1)

def mergesort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        left_inversions = mergesort(a, left, mid)
        right_inversions = mergesort(a, mid + 1, right)
        merge_inversions = merge(a, left, mid, right)
        return left_inversions + right_inversions + merge_inversions
    else:
        return 0

def merge(A, left, mid, right):
    i = left
    j = mid + 1
    inversions = 0
    temp = []

    while i <= mid and j <= right:
        if A[i] > A[j]:
            temp.append(A[j])
            inversions += (mid - i + 1)
            j += 1
        else:
            temp.append(A[i])
            i += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= right:
        temp.append(A[j])
        j += 1

    A[left:right+1] = temp
    return inversions

if __name__ == '__main__':
    A = [-1, 6, 3, 4, 7, 4]
    m = solution(A)
    print(m)


# Given array: A = [-1, 6, 3, 4, 7, 4]
# call merge(A, 0, 1, 2):

# i = 0 (left subarray)
# j = 2 (right subarray)
# inversions = 0
# temp = []

# Compare the elements at A[i] and A[j]:

# A[0] = -1 and A[2] = 3
# Since A[0] < A[2], we add A[0] to the temp array.
# i is incremented to 1.

# Compare the elements at A[i] and A[j]:

# A[1] = 6 and A[2] = 3
# Since A[1] > A[2], we add A[2] to the temp array and increment the inversions counter by 1 - 0 + 1 = 2
# (since all the elements in the left subarray from index 0 to 1 are greater than A[2]).
# j is incremented to 3.

# Compare the elements at A[i] and A[j]:

# A[1] = 6 and A[3] = 4
# Since A[1] > A[3], we add A[3] to the temp array and increment the inversions counter by 1 - 1 + 1 = 1
# (since all the elements in the left subarray from index 1 to 1 are greater than A[3]).
# j is incremented to 4.