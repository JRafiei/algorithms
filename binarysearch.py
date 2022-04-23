


def binary_search(items, target):
    start = 0
    end = len(items) - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if target == items[mid]:
            index = mid
            break
        elif target < items[mid]:
            end = mid - 1
        elif target > items[mid]:
            start = mid + 1

    return index


if __name__ == '__main__':
    items = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
    target = 15
    target_index = binary_search(items, target)
    if target_index != -1:
        print(f'{target} found at index{target_index}')
    else:
        print('Target not found')
