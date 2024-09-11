"""

"""

from collections import deque


def solution(begin, target, words):
    answer = 0
    word_dict = {}  #
    words.append(begin)
    N = len(words)

    visited = set()
    dist = {}

    def word_change(start):
        visited.add(start)
        dist[start] = 0
        queue = deque()
        queue.append(start)

        while queue:
            next_word = queue.popleft()
            for word in word_dict[next_word]:
                if word in visited: continue
                visited.add(word)
                queue.append(word)
                dist[word] = dist[next_word] + 1

    for word in words:
        word_dict[word] = []
        dist[word] = 0
        for comp in words:
            if word == comp: continue
            cnt = 0
            for i in range(len(begin)):
                if word[i] != comp[i]:
                    cnt += 1
                if cnt > 1: continue
            else:
                if cnt == 1:
                    word_dict[word].append(comp)

    # print(word_dict)
    # print(dist)
    word_change(begin)
    if target not in words:
        answer = 0
    else:
        answer = dist[target]

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


# 진문님 코드
# import sys
# from collections import deque
# # sys.stdin = open('input.txt')
#
# def solution(begin):
#     global cnt
#
#     # 문자열의 각 자리 char를 set에 모아서 하나씩 다 변환해서 비교하기
#     for i in range(len(begin)):
#         d_set = set()
#         for word in arr:
#             # 같은 char인 경우 early return
#             if word[i] == begin[i]: continue
#             d_set.add(word[i])
#         # 모여진 set값을 활용해 begin 인자 변환
#         for d in d_set:
#             comp = begin.replace(begin[i],d)
#             # 같으면 early return
#             if comp == begin: continue
#             # 이미 확인했던 char 또는 word early return1
#             # "hit", "cog"
#             # "hot", "dot", "dog", "lot", "log", "cog"
#             if comp in used_lst: continue
#             if comp in arr:
#                 # 타겟을 찾은 경우 재귀함수 종료
#                 if comp == tar:
#                     return
#                 q.append(comp)
#                 used_lst.append(comp)
#
#     #3. 재귀호출
#     solution(q.popleft())
#     cnt += 1
#
#
# T = int(input())
# for tc in range(1,T+1):
#     be, tar = map(str,input().split())
#     arr = input().split()
#     cnt = 0
#     # 확인했던 값 확인하기 위한 리스트
#     used_lst = []
#     q = deque()
#     # 타겟 문자열이 입력 리스트에 존재하지 않으면 재귀호출을 시작할 이유가 없음
#     if tar not in arr:
#         print(cnt)
#     else:
#         solution(be)
#         print(cnt)

# 1
# hit cog
# hot dot dog lot log cog


# 나영 DFS
def dfs(x, y):

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == 0 and visited[nx][ny] == 0:

            visited[nx][ny] = 1
            dfs(nx,ny)


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 우, 하, 좌, 상
ans = 0

for i in range(N):
    for j in range(M):

        if arr[i][j] == 0:
            if visited[i][j]:
                continue
            visited[i][j] = 1
            dfs(i, j)
            print(visited)
            ans += 1

print(visited)
print(ans)

"""
4 5
00110
00011
11111
00000

3 3
001
010
101
"""