def dfs(start, dictionary, arr, visited):
    for i in range(len(dictionary[start])):
        if visited[start][i]:
            continue
        arr.append(dictionary[start][i])
        visited[start][i] = 1
        dfs(dictionary[start][i], dictionary, arr, visited)
    return arr


def solution(tickets):
    airport_dict = {}
    visited = {}

    for ticket in tickets:
        for airport in ticket:
            if airport not in airport_dict:
                airport_dict.setdefault(airport, [])
                visited.setdefault(airport, [])

    N = len(airport_dict)
    print(N)

    for ticket in tickets:
        airport_dict[ticket[0]].append(ticket[1])
        visited[ticket[0]].append(0)

    for keys in airport_dict.keys():
        airport_dict[keys].sort()

    print(visited)
    print(airport_dict)
    path = [tickets[0][0]]
    answer = dfs(tickets[0][0], airport_dict, path, visited)
    return answer


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([['icn', 'jfk'], ['jfk', 'pus'], ['pus', 'jej'], ['jej', 'icn']]))