"""
서로 이어져 있지 않은 네트워크의 수를 구하는 문제입니다.
문제의 예시처럼 A - B가 하나로 이어져 있고, C 혼자 있으면 네트워크 수가 2가 되는 것입니다.
한 점에서 DFS를 실시한 후 DFS가 끝나도 방문하지 않은 점이 있다면
네트워크가 서로 이어져 있지 않다는 의미가 됩니다.
따라서 DFS를 시작하는 computer의 개수가 네트워크의 수가 된다고 생각하고 문제를 풀었습니다.
example
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
return = 2
    |0|
    |1|     |2|
0번째 computer부터 DFS를 시작하면 0번째, 1번째는 연결되어 있어 DFS 한 번에 두 computer를 방문하지만
2번째 computer는 연결되어 있지 않으므로, 2번째 computer에서 따로 DFS를 시작해야 해서
DFS를 실행하는 횟수인 2가 답이 됩니다.
"""


def network(num, n, visited, arr):
    visited[num] = 1    # 방문 표시

    for i in range(n):  # computers의 한 행을 반복 -> computers[0] = [1, 1, 0]
        if visited[i]:  # 방문한 적이 있으면 continue
            continue
        if arr[num][i]:  # 방문한 적이 없고, computers[num][i] = 1이라면 재귀로 DFS
            network(i, n, visited, arr)


def solution(n, computers):
    answer = 0  # 네트워크 수(덩어리 수)
    visited = [0] * n   # 방문 표시를 할 리스트

    for i in range(n):
        if not visited[i]:  # 방문한 적이 없다면
            network(i, n, visited, computers)   # DFS 실행
            answer += 1 # DFS 실행 횟수(네트워크 수)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))