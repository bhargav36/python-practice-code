def bubble_sort(arr):
    n = len(arr)
    sorted = True
    for i in range(n):

        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False

arr = [22,33,11,66,55,99,77,88,44]

bubble_sort(arr)

print("Sorted Array:")
for i in range(len(arr)):
    print("%d" %arr[i])