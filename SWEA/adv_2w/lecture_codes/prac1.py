# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

#
# def KFC(x):
#     KFC(x+1)
#
#
# KFC(0)
# print("end")

# def func(x):
#     if x == 6:
#         return
#     print(x, end=' ')
#     func(x + 1)
#     print(x, end=' ')
#
# start = 0
# func(start)

# 111 ~ 666
# def perm(num):
#     if num == 3:
#         print(*lst)
#         return
#
#     for i in range(1, 7):
#         lst.append(i)
#         perm(num + 1)
#         lst.pop()
#
#
# start = 0
# lst = []
# perm(start)

path = []
used = [0] * 7  # 1~6 숫자의 사용 여부를 기록할 리스트


def recur(level):
    if level == 3:
        print(*path)
        return
    # 2. 후보군을 반복하면서
    for i in range(1, 7):
        # i가 이미 뽑혔다면, pass 해라
        # 아래 코드의 단점 :  "in" = O(len(path))
        # 시간 초과 위험도가 높다!
        # if i in path:
        #     continue

        # 방문하지 않았다면 실행해라
        # == 방문했다면 실행하지 마라
        if used[i]:
            continue
        # 2.1 재귀 호출 전 - 경로 기록 + 사용 기록
        used[i] = 1
        path.append(i)
        # 2.2 다음 재귀 호출(파라미터 전달)
        recur(level + 1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제 + 사용 여부 초기화
        path.pop()
        used[i] = 0
recur(0)

# 11111 ~ 44444
# def perm(num):
#     if num == 5:
#         print(*lst)
#         return
#
#     for i in range(1, 5):
#         lst.append(i)
#         perm(num + 1)
#         lst.pop()
#
#
# start = 0
# lst = []
# perm(start)