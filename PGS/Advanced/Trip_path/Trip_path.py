def trip(start, dictionary, arr, visited):

    for i in range(len(dictionary[start])):
        if visited[start][i]:
            continue
        if not dictionary[dictionary[start][i]]:
            continue
        arr.append(dictionary[start][i])
        visited[start][i] = 1
        trip(dictionary[start][i], dictionary, arr, visited)

    return arr


def solution(tickets):
    airport_dict = {}
    visited = {}# 경로 중복도 있음

    for ticket in tickets:
        for airport in ticket:
            if airport not in airport_dict:
                airport_dict.setdefault(airport, [])
                visited.setdefault(airport, [])

    for ticket in tickets:
        airport_dict[ticket[0]].append(ticket[1])
        visited[ticket[0]].append(0)

    for keys in airport_dict.keys():
        airport_dict[keys].sort()

    print(visited)
    print(airport_dict)
    path = ["ICN"]
    answer = trip("ICN", airport_dict, path, visited)

    for keys in airport_dict.keys():
        for i in range(len(airport_dict[keys])):
            if not visited[keys][i]:
                answer.append(airport_dict[keys][i])
    return answer


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["SFO", "ATL"], ["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution([["ICN", "AAA"], ["DDD", "ICN"], ["ICN", "DDD"]]))
# print(solution([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "CCC"], ["CCC", "ICN"], ["ICN", "DDD"], ["DDD", "AAA"]]))
print(solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]]))
