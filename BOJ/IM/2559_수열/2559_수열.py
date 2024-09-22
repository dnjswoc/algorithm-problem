# 시간 복잡도를 줄일 수 없음...
import sys
sys.stdin = open('input_1.txt', 'r')

N, K = map(int, input().split())
temp_arr = list(map(int, input().split()))
seq_temp_arr = [0] * (N - K + 1)    # window 사이즈만큼 0 배열 생성

for i in range(N - K + 1):  # window 사이즈만큼 순회
    sum_temp = 0    # 하나의 window 안의 온도 합계
    for j in range(K):
        sum_temp += temp_arr[i + j]
    seq_temp_arr[i] = sum_temp  # window 마다의 온도 합을 seq_temp_arr 리스트에 저장

for k in range(N - K):  # seq_temp_arr 리스트의 최댓값을 구하기 위함
    if seq_temp_arr[k] > seq_temp_arr[k + 1]:
        seq_temp_arr[k], seq_temp_arr[k + 1] = seq_temp_arr[k + 1], seq_temp_arr[k]

print(seq_temp_arr[-1])

# 건수 방법
N, K = map(int, input().split())
num_lst = list(map(int, input().split()))
current_sum = sum(num_lst[0:K])
max_sum = current_sum

for i in range(N - K):
    current_sum = current_sum - num_lst[i] + num_lst[i + K]
    if max_sum <= current_sum:
        max_sum = current_sum

print(max_sum)