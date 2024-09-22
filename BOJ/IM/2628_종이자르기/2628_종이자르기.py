import sys
sys.stdin = open('input.txt', 'r')


def arr_sort(arr):      # 리스트 내림차순으로 정렬
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def max_len(arr):   # 내림차순으로 정렬된 리스트를 통해 가장 긴 길이를 구하는 함수
    len_arr = []
    for i in range(len(arr) - 1):
        len_arr.append(arr[i] - arr[i + 1])  # 한 칸 씩 빼서 자르고 난 길이를 구한다.
    for i in range(len(len_arr) - 1):
        if len_arr[i] > len_arr[i + 1]:  # 자르고 난 길이 중 최댓값 구하기
            len_arr[i], len_arr[i + 1] = len_arr[i + 1], len_arr[i]
    return len_arr[-1]  # 최댓값 return


N, M = map(int, input().split())
C = int(input())
cut_arr = [list(map(int, input().split())) for _ in range(C)]
width_arr = [0, N]  # 가로 길이들을 구하기 위한 리스트
height_arr = [0, M]  # 세로 길이들을 구하기 위한 리스트
for cut in cut_arr:  # 입력 값 반복
    if cut[0] == 0:  # 세로 리스트에 추가
        height_arr.append(cut[1])
        continue
    width_arr.append(cut[1])    # 가로 리스트에 추가
max_width = max_len(arr_sort(width_arr))
max_height = max_len(arr_sort(height_arr))
print(max_width*max_height) # 가로 길이 최댓값과 세로 길이 최댓값을 곱한다.
