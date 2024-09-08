def solution(tickets):
    airport_dict = {}

    for ticket in tickets:
        for airport in ticket:
            if airport not in airport_dict:
                airport_dict.setdefault(airport, [])

    N = len(airport_dict)
    print(airport_dict)
    print(N)

    # for
    answer = []
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
