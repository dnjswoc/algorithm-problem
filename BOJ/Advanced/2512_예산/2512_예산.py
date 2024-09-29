N = int(input())
budget_lst = list(map(int, input().split()))
M = int(input())

if sum(budget_lst) > M:
    
    pass
else:
    answer = max(budget_lst)

print(answer)
