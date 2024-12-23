import sys
sys.stdin = open('input.txt', 'r')

'''
어려운 문제였습니다... 제가 생각한 방법은 아래와 같습니다.
국가예산의 총합이 M으로 주어졌고, 이를 자방의 수 N으로 나누어줍니다.
그러면 각 지방에 나누어줄 수 있는 평균 예산이 나오는데 이를 넘지 않는 지방 예산은 온저히 배정해주고,
이를 넘는 지방 예산은 평균 예산을 넘지 않는 지방에 나누어주고 남은 국가예산에서 평균 예산을 넘는 지방의 수로 나누어주어
이를 지방 예산으로 배정해주는 것이었습니다.
N = 4
budget_lst = [120, 110, 140, 150]
M = 485
평균 예산 = 130
120, 110의 지방 예산은 그대로 배정해주고,
140, 150을 요청한 지방은 위에서 배정해주고 남은 예산 255를 2로 나누어준 127을 배정해줍니다.
하지만 여러 반례들에 부딪히며 결국 통과하지 못했습니다...

'''


# 이진탐색으로 평균 바로 아래의 인덱스를 구한다.
def binary(n, lst, key):
    low, high = 0, N - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return high


# 답을 구하는 함수
def budget(N, budget_lst, M):
    # 지방의 예산 요청의 합이 국가예산의 총합보다 크면 예산을 조절하여 배정해준다.
    if sum(budget_lst) > M:
        # 예산 오름차순 정렬
        budget_lst = sorted(budget_lst)

        avg_budget = sum(budget_lst) // N

        # 예산의 평균이 국가 예산의 총합보다 크면 지방에서 요청한 예산을 모두 줄 수 없어 국가예산의 평균을 배정한다.
        if avg_budget > M:
            return M // N

        # 그렇지 않다면 평균보다 작은 예산 먼저 배정해주고 평균을 넘는 예산은 배정해주고 남은 예산을 나눠준다.
        avg_idx = binary(N, budget_lst, avg_budget)
        small_lst = budget_lst[:avg_idx + 1]
        over_budget = M - sum(small_lst)

        return over_budget // (N - len(small_lst))

    # 예산 총합이 국가예산 보다 작으면 예산을 모두 배정해줄 수 있으므로 예산의 최댓값을 출력
    else:
        return max(budget_lst)


N = int(input())
budget_lst = list(map(int, input().split()))
M = int(input())

answer = budget(N, budget_lst, M)

print(answer)


# 나영이 코드
# N = int(input()) # 지방의 수
# bg_li = list(map(int,input().split()))  # 각 국가별 원하는 예산 리스트 목록
# total_bg = int(input())
#
# if sum(bg_li) <= total_bg:  # 리스트 합이 국가예산 총합보다 같거나 작으면 조건 1 충족 그냥 max값 찾아버림
#     print(f'{max(bg_li)}')
#
# else:
#     bg = total_bg//len(bg_li)  # 각 나라별 가능한 예산 수치  :121
#     diff = 0  # 12
#     cnt = 0
#     for li in bg_li:
#         if li > bg: continue
#         diff += abs(li-bg)  # 최대 상한액 구하기 위해 차이값 구함
#         cnt += 1  # 예산 오바되는 국가 갯수 카운팅 위함
#
#     if cnt == 0:
#         print(f'{bg}')
#     else:
#         max_bg = bg + (diff//cnt)  # 최대 상한액
#         print(f'{max_bg}')
