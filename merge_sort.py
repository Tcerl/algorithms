def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Tìm chỉ số giữa
        left_half = arr[:mid]  # Chia mảng thành 2 phần
        right_half = arr[mid:]

        merge_sort(left_half)   # Sắp xếp nửa bên trái
        merge_sort(right_half)  # Sắp xếp nửa bên phải

        # Trộn hai mảng con đã sắp xếp
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Sao chép phần còn lại nếu có
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ví dụ sử dụng:
arr = [8, 3, 7, 4, 9, 2]
merge_sort(arr)
print("Mảng sau khi sắp xếp:", arr)
