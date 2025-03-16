def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Lặp qua từng phần tử
        min_index = i  # Giả sử phần tử hiện tại là nhỏ nhất
        for j in range(i + 1, n):  # Tìm phần tử nhỏ nhất trong phần còn lại
            if arr[j] < arr[min_index]:
                min_index = j  # Cập nhật chỉ mục của phần tử nhỏ nhất
        if min_index != i:  # Nếu tìm thấy phần tử nhỏ hơn, hoán đổi
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Ví dụ sử dụng:
arr = [5, 3, 8, 4, 2]
selection_sort(arr)
print("Mảng sau khi sắp xếp:", arr)
