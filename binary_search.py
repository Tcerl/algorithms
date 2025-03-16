# Cach 1:
def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1  # Không tìm thấy

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid  # Tìm thấy phần tử

    if arr[mid] > target:
        return binary_search_recursive(arr, left, mid - 1, target)  # Tìm bên trái

    return binary_search_recursive(arr, mid + 1, right, target)  # Tìm bên phải

# Ví dụ sử dụng:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

print(f"Phần tử {target} nằm ở vị trí {result}" if result != -1 else "Không tìm thấy")

# Cach 2:
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Tìm thấy

        if arr[mid] > target:
            right = mid - 1  # Dịch phạm vi về bên trái
        else:
            left = mid + 1  # Dịch phạm vi về bên phải

    return -1  # Không tìm thấy

arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_iterative(arr, target)

print(f"Phần tử {target} nằm ở vị trí {result}" if result != -1 else "Không tìm thấy")
