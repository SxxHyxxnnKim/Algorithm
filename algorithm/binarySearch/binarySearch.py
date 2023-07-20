def binary_search(start, end , target, array):
    while start <= end:
        #중간값
        mid =(start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            # end = mid -> 무한 루프에 갇힐 수 있음
            end = mid - 1
        else:
            start = mid + 1
        
        return None

array = [1, 2, 3, 4, 5]
target = 5
result = binary_search(0, len(array) -1, target, array)

print(result)