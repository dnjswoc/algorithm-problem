import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def sort_score(arr):                # 성적을 내림차순으로 정렬하는 함수
    for i in range(N-1, 0, -1):     # bubble sort
        for j in range(0, i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


for test_case in range(T):
    N, K = map(int, input().split())    # N : 시험 친 과목 수, K : 선택할 수 있는 과목 수
    scores = list(map(int, input().split()))    # 성적 입력
    sorted_score = sort_score(scores)   # 성적을 내림차순으로 정렬
    max_score = 0                       # 최대 총점
    for k in range(K):                  # 가장 큰 성적을 k개 추출하여 덧셈
        max_score += sorted_score[k]
    print(f'#{test_case+1} {max_score}')    # output 출력
