# hoare 방식의 퀵 소트


def hoare_partition(left, right):   # 개념적으로 배운 quick sort
    pivot = arr[left]   # pivot은 왼쪽, 오른쪽, 가운데 어디두든 상관없다.
    left += 1
    '''
       left                 right
        ↓                    ↓
    [3, 2, 4, 6, 9, 1, 8, 7, 5]
     ↑
     p
    '''
    while True:
        # left index가 right index보다 작고
        while left <= right and arr[left] < pivot:
            # 그 left 번째 값이 pivot보다 작다면,
            left += 1   # left는 4에 고정
        while left <= right and arr[right] > pivot:
            right -= 1  # right 1에 고정
        # left와 right가 엇갈린 상황이 발생한다면, 두 위치는 swap하지 않고
        if left >= right:
            return right    # pivot_index가 된다.
        arr[left], arr[right] = arr[right], arr[left]   # 1, 4 교환



# left : 왼쪽 정렬 대상 시작 지점
# right : 오른쪽 정렬 대상 시작 지점
def quick_sort(left, right):
    # 조사 대상이 하나 이하가 된다면, 더 이상 조사 할 수 없음
    if left >= right: return

    # 호어 방식의 정렬을 위해서는, 정렬을 위한 배열을
    # 영역별로 구분 지을 수 있어야 하고,
    # 호어 방식의 파티션 구분 결과로 얻은 index 지점을 pivot으로 보겠다.
    pivot_index = hoare_partition(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    print(arr)

    quick_sort(left, pivot_index - 1)
    quick_sort(pivot_index + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
