# Adopted from https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr1,arr2):
    if len(arr1) > 1:
 
         # Finding the mid of the array
        mid = len(arr1)//2

        L1 = arr1[:mid]
        L2 = arr2[:mid]
        R1 = arr1[mid:]
        R2 = arr2[mid:]

        mergeSort(L1, L2)
        mergeSort(R1, R2)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L1) and j < len(R1):
            if L1[i] < R1[j]:
                arr1[k] = L1[i]
                arr2[k] = L2[i]
                i += 1
            else:
                arr1[k] = R1[j]
                arr2[k] = R2[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L1):
            arr1[k] = L1[i]
            arr2[k] = L2[i]
            i += 1
            k += 1
 
        while j < len(R1):
            arr1[k] = R1[j]
            arr2[k] = R2[j]
            j += 1
            k += 1


if __name__ == '__main__':
    line = list(map(int, input().split()))
    N = line[0]
    k = line[1]
    names = []
    expressions = []
    for i in range(N):
      name, expr = input().split()
      names.append(name)
      expressions.append(float(expr))
    mergeSort(expressions, names)
    # n - k because we have increasing sorting
    print(names[N - k])