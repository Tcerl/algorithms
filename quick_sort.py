def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)  # Sắp xếp bên trái pivot
        quick_sort(arr, pivot_index + 1, right) # Sắp xếp bên phải pivot

def partition(arr, left, right):
    pivot = arr[right]  # Chọn phần tử cuối cùng làm pivot
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Hoán đổi phần tử nhỏ hơn pivot lên trước
    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Đưa pivot vào vị trí đúng
    return i + 1  # Trả về vị trí mới của pivot

# Ví dụ sử dụng:
arr = [8, 3, 7, 4, 9, 2]
quick_sort(arr, 0, len(arr) - 1)
print("Mảng sau khi sắp xếp:", arr)
