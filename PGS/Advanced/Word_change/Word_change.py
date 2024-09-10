def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
