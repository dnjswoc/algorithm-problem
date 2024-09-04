# lomuto
def lomuto_partition(left, right):
    idx = left - 1  # 모든 상황에 대해서 동일하게 코드를 작성
    pivot = arr[right]  # lomuto 방식은 for문으로 처리

    # right 번째 -> pivot, range(l, right) -> right - 1
    for next in range(left, right):
        if arr[next] < pivot:
            idx += 1
            arr[idx], arr[next] = arr[next], arr[idx]

    arr[idx + 1], arr[right] = arr[right], arr[idx + 1]
    return idx + 1


def quick_sort(left, right):
    if left < right:
        pivot_idx = lomuto_partition(left, right)

        quick_sort(left, pivot_idx - 1)
        quick_sort(pivot_idx + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
