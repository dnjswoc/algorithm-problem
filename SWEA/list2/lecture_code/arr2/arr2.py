# arr1 = [0] * 3
# print(arr1)
# arr2 = [[0] * 3 for _ in range(2)]
# for i in range(2):
#     print(arr2[i])
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end='')

# arr = [[1, 2, 3], [4, 5, 6]]
# print(len(arr))
# print(len(arr[0]))

arr = [list(map(int, input().split())) for _ in range(5)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
sum_diag = 0
for i in range(5):
    sum_diag = sum_diag + arr[i][i] + arr[4-i][i]
sum_diag -= arr[2][2]
print(sum_diag)

