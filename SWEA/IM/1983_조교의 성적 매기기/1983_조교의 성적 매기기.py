# 14:20 - 15:30
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def tot_score():        # 총점을 구하는 함수
    new_arr = []
    for score in score_arr:
        total_sum = (score[0] * 0.35) + (score[1] * 0.45) + (score[2] * 0.2)
        new_arr.append(total_sum)
    return new_arr, new_arr[K - 1]  # 총점을 저장한 리스트와 성적을 구하고 싶은 점수 return


def score_sort(arr):        # 총점을 정렬하는 함수
    for i in range(N-1, 0, -1):  # 버블 정렬
        for j in range(0, i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def score_output(score):    # 성적을 구하고 싶은 점수의 총점에서의 위치를 통해 성적을 구하는 함수
    for num in range(N):
        if sorted_score[num] == score:
            if 0 < (num + 1) / N <= 0.1:
                return 'A+'
            elif (num + 1) / N <= 0.2:
                return 'A0'
            elif (num + 1) / N <= 0.3:
                return 'A-'
            elif (num + 1) / N <= 0.4:
                return 'B+'
            elif (num + 1) / N <= 0.5:
                return 'B0'
            elif (num + 1) / N <= 0.6:
                return 'B-'
            elif (num + 1) / N <= 0.7:
                return 'C+'
            elif (num + 1) / N <= 0.8:
                return 'C0'
            elif (num + 1) / N <= 0.9:
                return 'C-'
            else:
                return 'D0'


for test_case in range(T):
    N, K = map(int, input().split())
    score_arr = [list(map(int, input().split())) for _ in range(N)]
    total_score, score_K = tot_score()
    sorted_score = score_sort(total_score)
    print(f'#{test_case+1} {score_output(score_K)}')
