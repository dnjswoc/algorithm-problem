import sys
sys.stdin = open('input.txt')


def dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    v = s
    result = [s]
    visited[s] = 1
    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack += [v]
                v = w
                result += [v]
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return result


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1] += [v2]
    adjL[v2] += [v1]
answer = dfs(1, V)
print(f'#1 {answer}')
