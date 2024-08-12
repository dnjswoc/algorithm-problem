# import sys
# sys.stdin = open('input.txt')


def dfs(s, V):                      # DFS 함수 정의(s : 시작값, V : 최대 정점값)
    visited = [0] * (V+1)           # 방문 흔적 남기기 위한 리스트
    stack = []                      # 스택 생성
    v = s                           # 시작값을 v에 저장
    result = [s]                    # result 리스트에 시작값 저장
    visited[s] = 1                  # 출발 지점을 방문 기록
    while True:                     # 참일 동안 반복
        for w in adjL[v]:           # 인접 리스트의 요소 반복
            if visited[w] == 0:     # 방문한 적 없으면
                stack += [v]        # 스택 push
                v = w               # v에 w값 저장
                result += [v]       # result 리스트에 v 저장
                visited[w] = 1      # 방문 기록 남기기
                break               # 반복문 탈출
        else:                       # 반복문을 다 돌면
            if stack:               # 스택이 빈 리스트가 아니면
                v = stack.pop()     # 마지막 인덱스 pop
            else:                   # 빈 리스트라면
                break               # while 문 종료
    answer_str = ''                 # 답으로 제출할 리스트 문자열로 변환
    for i in result:
        answer_str += str(i)
    return answer_str               # 문자열 return


V, E = map(int, input().split())    # 최대 정점 개수, 간선의 개수 입력
arr = list(map(int, input().split()))   # 간선의 개수만큼 연결된 두 정점들 입력
adjL = [[] for _ in range(V+1)]     # 인접 리스트 생성
for i in range(E):                  # 인접 리스트 작성
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1] += [v2]
    adjL[v2] += [v1]
answer = dfs(1, V)                  # DFS 함수 호출
print(f'#1', end=' ')               # output 출력
print('-'.join(answer))
