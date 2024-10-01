import sys
sys.stdin = open('input.txt', 'r')


# 이진탐색으로 평균 바로 아래의 인덱스를 구한다.
# def binary(n, lst, key):
#     low, high = 0, N - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == key:
#             return mid
#         elif lst[mid] > key:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return high
#
#
# def budget(N, budget_lst, M):
#     if sum(budget_lst) > M:
#         # 예산 오름차순 정렬
#         budget_lst = sorted(budget_lst)
#
#         avg_budget = sum(budget_lst) // N
#
#         if avg_budget > M:
#             return M // N
#
#         avg_idx = binary(N, budget_lst, avg_budget)
#         small_lst = budget_lst[:avg_idx + 1]
#         over_budget = M - sum(small_lst)
#
#         return over_budget // (N - len(small_lst))
#
#     # 예산 총합이 국가예산 보다 작으면 예산의 최댓값 출력
#     else:
#         return max(budget_lst)
#
#
# N = int(input())
# budget_lst = list(map(int, input().split()))
# M = int(input())
#
# # 예산 총합이 국가예산보다 크면
# answer = budget(N, budget_lst, M)
#
# print(answer)


# 나영이 코드
N = int(input()) # 지방의 수
bg_li = list(map(int,input().split()))  # 각 국가별 원하는 예산 리스트 목록
total_bg = int(input())

if sum(bg_li) <= total_bg:  # 리스트 합이 국가예산 총합보다 같거나 작으면 조건 1 충족 그냥 max값 찾아버림
    print(f'{max(bg_li)}')

else:
    bg = total_bg//len(bg_li)  # 각 나라별 가능한 예산 수치  :121
    diff = 0  # 12
    cnt = 0
    for li in bg_li:
        if li > bg: continue
        diff += abs(li-bg)  # 최대 상한액 구하기 위해 차이값 구함
        cnt += 1  # 예산 오바되는 국가 갯수 카운팅 위함

    if cnt == 0:
        print(f'{bg}')
    else:
        max_bg = bg + (diff//cnt)  # 최대 상한액
        print(f'{max_bg}')
