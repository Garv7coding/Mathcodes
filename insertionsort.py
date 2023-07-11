def insertionSort(alist):
    for step in range(1, len(alist)):
        key = alist[step]
        j = step - 1
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = key


data = [9, 6, 2, 3, 8, 4, 1]
print(f"List to sort: {data}")
insertionSort(data)
print('Sorted List in Ascending Order:')
print(data)