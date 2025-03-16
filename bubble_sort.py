def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Lặp qua từng phần tử
        swapped = False
        for j in range(n - i - 1):  # So sánh phần tử kề nhau
            if arr[j] > arr[j + 1]:  # Nếu sai thứ tự, hoán đổi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Nếu không có hoán đổi nào, dừng vòng lặp
            break

arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print("Mảng sau khi sắp xếp:", arr)
