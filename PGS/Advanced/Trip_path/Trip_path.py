"""
스터디 시작하면서 푼 문제 중에서 제일 어려웠습니다ㅠㅠ
처음 접근할 때는 괜찮아 보였지만 풀면 풀수록 늪에 빠지듯이 오답 행렬에서 빠져 나오지 못했습니다
저는 처음 문제를 접근할 때 2차원 배열로 항공편이 주어지고,
각 항공편은 ['출발 공항', '도착 공항']으로 주어졌습니다.
그래서 저는 출발 공항을 key로 가지고, 도착 공항을 value로 가지는 딕셔너리를 만들어
인접 리스트와 같은 느낌으로 사용하려고 했습니다.
그리고 알파벳 순서가 빠른 공항부터 먼저 도착하기 때문에 딕셔너리의 value들을 각각 정렬했습니다.
ex.
tickets = [["SFO", "ATL"], ["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
airport_dict = {'SFO': ['ATL'], 'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO']}
visited = {'SFO': [0], 'ATL': [0, 0], 'ICN': [0, 0]}
그리고 각 출발 공항에서 도착 공항으로 갔다(항공편 소모)는 방문 표시를 위한 visited 딕셔너리도 만들었습니다.
이렇게 주어진 배열을 전처리 하고, 문제에서 항상 "ICN"에서 출발한다고 했기 때문에
"ICN"을 시작 노드로 하는 DFS를 실행하면 되겠다고 생각하고 문제를 풀기 시작했습니다.
"""

def trip(start, dictionary, arr, visited):

    for i in range(len(dictionary[start])):     # 딕셔너리의 도착 공항 리스트 길이만큼 반복
        if visited[start][i]:   # 이미 사용한 항공편이라면(ex. "ICN" -> "ATL") continue
            continue
        # 다음으로 출발할 항공편의 도착 공항이 없다면(다음으로 갈 곳이 없다면, ex. "ICN" -> "AAA" -> "") continue
        if not dictionary[dictionary[start][i]]:
            continue
        arr.append(dictionary[start][i])    # arr(path, 경로)에 도착 공항을 추가
        visited[start][i] = 1   # 항공편을 사용했다고 표기(ex. visited = {"ICN" : [1, 0], ...})
        trip(dictionary[start][i], dictionary, arr, visited)    # 그 다음 항공편에 대하여 재귀

    return arr  # arr(path) return


def solution(tickets):
    airport_dict = {}   # 출발 공항과 도착 공항을 기록한 딕셔너리
    visited = {}    # 도착 공항의 방문 표시를 위한 딕셔너리

    for ticket in tickets:  # 항공편을 반복하고
        for airport in ticket:  # 항공편의 공항을 반복하며
            if airport not in airport_dict:  # 딕셔너리에 공항명이 없다면
                airport_dict.setdefault(airport, [])    # 공항명을 key로 하고 빈 리스트를 value로 하여 추가
                visited.setdefault(airport, [])     # visited도 공항명을 key로 하고 빈 리스트를 value로 하여 추가

    for ticket in tickets:
        airport_dict[ticket[0]].append(ticket[1])   # 출발 공항을 key로 할 때 도착 공항을 value에 추가
        visited[ticket[0]].append(0)    # visited도 출발 공항을 key로 할 때 value에 도착 공항의 수 만큼 0 추가

    # airport_dict = {'SFO': ['ATL'], 'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO']}
    # visited = {'SFO': [0], 'ATL': [0, 0], 'ICN': [0, 0]}

    for keys in airport_dict.keys():
        airport_dict[keys].sort()   # 도착 공항을 알파벳 순으로 정렬

    # print(visited)
    # print(airport_dict)

    path = ["ICN"]  # 시작 공항을 기록, 항상 인천 공항에서 출발하므로 "ICN" 저장
    answer = trip("ICN", airport_dict, path, visited)   # 출발 공항과 공항 딕셔너리, 경로, visited를 매개변수로 DFS

    for keys in airport_dict.keys():
        for i in range(len(airport_dict[keys])):
            if not visited[keys][i]:    # 사용하지 않은 항공편이 있다면
                answer.append(airport_dict[keys][i])    # 마지막으로 경로에 추가
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["SFO", "ATL"], ["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution([["ICN", "AAA"], ["DDD", "ICN"], ["ICN", "DDD"]]))
print(solution([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "CCC"], ["CCC", "ICN"], ["ICN", "DDD"], ["DDD", "AAA"]]))
print(solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]]))


# 나영이 코드
def solution(tickets):
    def dfs(start, ans):

        for i in range(len(road_dict[start])):
            if road_dict[start][i] not in road_dict.keys():
                ans.append(road_dict[start][i])
                return
            if visited[start][i]:   # 사용한 항공편이라면 continue
                continue
            visited[start][i] = 1   # 아니라면 방문 표시
            ans.append(road_dict[start][i])
            dfs(road_dict[start][i], ans)

    visited = {}
    for s, v in tickets:
        if s in visited:
            visited[s].append(0)
        else:
            visited[s] = [0]
    print(visited)

    ans = []
    start = "ICN"
    road_dict = {}  # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}

    for s, v in tickets:
        if s in road_dict:
            road_dict[s].append(v)
        else:
            road_dict[s] = [v]

    for key in road_dict.keys():  # 문제에서 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return 위해 sort작업처리
        road_dict[key].sort()
    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    ans.append(start)  # 인천 출발

    dfs(start, ans)

    return ans


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["SFO", "ATL"], ["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
