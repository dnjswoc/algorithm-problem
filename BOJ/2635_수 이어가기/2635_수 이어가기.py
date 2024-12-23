N = int(input())
max_num_list = [0] * N

for i in range(1, N + 1):
    num_list = [N, i]       # 첫 번째 수와 두 번째 수를 미리 리스트에 저장
    while num_list[-1] >= 0:    # 리스트의 마지막 값이 0보다 작아질 때까지 반복
        if num_list[-2] - num_list[-1] < 0:  # 리스트 뒤에서 두 번째 값 - 마지막 값이 0보다 작으면 반복문 탈출
            break
        num_list.append(num_list[-2] - num_list[-1])    # 아니면 리스트에 저장
    max_num_list[i-1] = [len(num_list), num_list]   # max_num_list에 num_list의 길이와 num_list 저장

for j in range(N - 1):  # 가장 큰 값만 알면 되므로 반복문을 1번만 쓴다.
    if max_num_list[j][0] > max_num_list[j + 1][0]:
        max_num_list[j], max_num_list[j + 1] = max_num_list[j + 1], max_num_list[j]
        # num_list의 길이로 정렬하면서 num_list도 같이 정렬

print(max_num_list[-1][0])
print(*max_num_list[-1][1])
