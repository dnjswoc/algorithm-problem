import sys
sys.stdin = open('input.txt', 'r')

'''
기타 레슨 문제도 굉장하네요...ㅎㅎ
이 문제는 녹화할 블루레이 개수가 M으로 주어지고, N개의 강의를 저장해야합니다.
주어진 순서대로 강의를 저장해야하며 N개의 강의를 M개의 그룹으로 나누어
각 그룹의 강의 시간 합을 그룹 평균 강의 시간(N / M)과의 차를 구해
차의 합이 가장 적은 그룹을 만들고, 그 그룹에서의 최댓값을 녹화할 블루레이의 최소 크기라고 생각했습니다.
ex.
N = 9, M = 3
average = 15 (N / M)
lectures = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group = [[1, 2, 3, 4, 5], [6, 7], [8, 9]]
sum_group = [15, 13, 17]
diff = [0, 2, 2]
answer = 17
'''


# M개의 블루레이에 저장할 조합을 정하고, 차가 최소가 될 때의 그룹의 최대 강의 시간 합을 구합니다.
def list_combination(s, m, sum_lst, sum_br):
    global answer
    global min_br

    # 강의 시간 차의 합이 이전 최소 시간 합보다 크면 return(백트래킹)
    if sum_br > min_br:
        return

    # 그룹의 개수가 M개가 되면 그룹별 강의 시간 합의 차를 비교
    if m == M:
        diff = abs(sum(lectures[s - 1:]) - avg_br)
        sum_lst.append(sum(lectures[s - 1:]))
        sum_br += diff

        # 강의 시간 합의 차가 최솟값 보다 작으면 최솟값 변경 및 정답도 같이 변경
        if min_br >= sum_br:
            min_br = sum_br
            answer = max(sum_lst)

        # 다음 케이스를 구하기 위해 pop(방문 표시 취소와 같은 느낌)
        sum_lst.pop()

    # lectures 리스트의 첫번째 값부터 순서대로 모두 빠짐없이 넣어야하므로
    for i in range(s, N - (M - m)):
        diff = abs(sum(lectures[s - 1:i]) - avg_br)
        sum_lst.append(sum(lectures[s - 1:i]))
        list_combination(i + 1, m + 1, sum_lst, sum_br + diff)
        sum_lst.pop()


N, M = map(int, input().split())
lectures = list(map(int, input().split()))

blu_ray = []    # 블루레이 그룹별 강의 시간 합을 저장할 리스트
min_br = sum(lectures)  # 최솟값 초기화(lectures의 합으로 했습니다)
avg_br = min_br / M  # 그룹별 강의 시간 합의 평균
answer = 0

list_combination(1, 1, blu_ray, 0)

print(answer)
