


def merge_sort(items):
    if len(items) < 2:
        return items

    start = 0
    end = len(items) - 1
    middle = (start + end) // 2
    left = items[:middle + 1]
    right = items[middle + 1:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    sorted_items = merge(sorted_left, sorted_right)
    return sorted_items


def merge(array1, array2):
    merged_array = []
    i = 0
    j = 0
    while True:
        if array1[i] <= array2[j]:
            merged_array.append(array1[i]) 
            i += 1
        else:
            merged_array.append(array2[j]) 
            j += 1

        if i == len(array1):
            merged_array.extend(array2[j:])
            break
        if j == len(array2):
            merged_array.extend(array1[i:])
            break
    return merged_array


if __name__ == '__main__':
    items = [18, 45, 33, 23, 9, 29, 13, 32, 6, 49, 7, 37, 7, 46, 44]
    sorted_items = merge_sort(items)
    print(items)
    print(sorted_items)
