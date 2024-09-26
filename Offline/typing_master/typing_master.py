import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
from itertools import permutations

N = int(input())    # N : 팀 개수
S, P = map(int, input().split())    # S : 강사님 점수, P : 강사님 정확도
student_score = [list(input().split()) for _ in range(2*N)]   # 학생 점수
print(student_score)


# 강사님 점수
t_score = int(S * (P/100))
# 강사님 점수 자릿수
t_score_length = len(str(t_score))

# 개인 점수 구하기
score_lst = []
for lst in student_score:
    # 타자 속도 * 정확도
    score = int(lst[0]) * (int(lst[1])/100)
    # 만약 한글로 했으면 0.7 곱해주기
    if lst[2] == 'K':
        score *= 0.7
    score_lst.append(int(score))

# 팀 별 평균 점수 구하기
# 원점수
current_score = {}
team_score = {}
# 강사님 점수와의 점수 차이
diff = []

for i in range(N):
    # 팀장과 팀원의 점수 평균
    current_score[i+1] = int((score_lst[2 * i] + score_lst[2 * i + 1])/2)
    team_score[i + 1] = str(current_score[i + 1]).zfill(t_score_length)

    split_score = list(team_score[i + 1])

    # 순열 구하기
    nPr = list(permutations(split_score, 3))
    min_diff = 1000

    # 강사님 점수와 가장 적은 점수 차이 구하기
    for num in nPr:
        case = 0
        for j in range(3):
            case += int(num[j])*(10**j)
            if abs(t_score - case) < min_diff:
                min_diff = abs(t_score - case)

    # 각 팀별 최소 점수 차이를 리스트에 저장
    diff.append([i +1, min_diff])

diff = sorted(diff, key=lambda x:x[1])
print(diff)
print(current_score)

for i in range(N - 1):
    for j in range(i + 1, N):
        if diff[i][1] != diff[j][1]: continue
        if current_score[diff[i][0]] < current_score[diff[j][0]]:
            diff[i], diff[j] = diff[j], diff[i]

for i in range(N):
    print(f'{i + 1}등: {student_score[(diff[i][0] - 1) * 2][-1]} {student_score[(diff[i][0] - 1) * 2 + 1][-1]} ({diff[i][0]} 팀)'
          f' | 점수 차 : {diff[i][1]} | 원점수: {current_score[diff[i][0]]}')


