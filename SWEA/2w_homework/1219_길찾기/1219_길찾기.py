import sys
sys.stdin = open('input.txt')


def dfs(s, V):                      # DFS 함수 정의(s : 출발 정점, V : 최대 정점)
    v = s                           # v에 출발 정점 저장
    visited = [0] * (V+1)           # 방문 흔적을 남기기 위한 리스트 생성
    visited[v] = 1                  # 출발 정점의 방문 흔적 남기기
    stack = []                      # 스택 생성
    while True:                     # DFS로 모든 경로 탐색
        for w in adjL[v]:
            if visited[w] == 0:
                stack += [v]
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    if visited[-1] == 1:            # 모든 경로 탐색 후 99를 거친 적이 있으면
        return True                 # return True                              
    else:                           # 그렇지 않으면
        return False                # return False


for _ in range(10):                         # 테스트 케이스 10번 반복
    T, E = map(int, input().split())        # T : 테스트 케이스 넘버, E : 간선 개수
    arr = list(map(int, input().split()))   # 순서쌍 입력
    V = 99                                  # 최대 정점
    adjL = [[] for _ in range(V+1)]         # 인접 리스트 생성
    for i in range(E):                      # 인접 리스트 만들기
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1] += [v2]
    if dfs(0, V):                           # 함수 return value가 true이면
        print(f'#{T} 1')                    # 1 출력
    else:                                   # 함수 return value가 false이면
        print(f'#{T} 0')                    # 0 출력
