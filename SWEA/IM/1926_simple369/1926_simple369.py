N = int(input())                            # 정수 입력
num_arr = list(range(1, N+1))               # 1부터 입력 받은 정수까지 리스트로 저장 
print_arr = [0] * N                         # 출력할 빈 리스트 생성

for num in range(N):                        # 입력 받은 정수만큼 반복
    count_369 = 0                           # 369 개수 count
    while num_arr[num] // 10 != 0:          # 10으로 나누어 1의 자리가 될 때까지 반복 
        if (num_arr[num] % 10 == 3) or (num_arr[num] % 10 == 6) or (num_arr[num] % 10 == 9):    # 마지막 자리에 369가 있으면
            count_369 += 1                  # count 1씩 증가
        num_arr[num] //= 10                 # 마지막 자리 제거
    if (num_arr[num] % 10 == 3) or (num_arr[num] % 10 == 6) or (num_arr[num] % 10 == 9): 
        count_369 += 1                      # while문이 끝나고 난 뒤 1의 자리에서 369가 있으면 count 1씩 증가
    if count_369 > 0:                       # count가 0보다 크면
        print_arr[num] = '-'*count_369      # 리스트에 count 개수만큼 '-' 저장
    else:                                   # 숫자에 369가 없으면
        print_arr[num] = num + 1            # 리스트에 숫자 그대로 저장
    print(print_arr[num], end=' ')          # output 출력
