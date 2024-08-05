# import sys
# sys.stdin = open('input.txt')

T = int(input())                                # 테스트 케이스 입력

for test_case in range(T):                      # 테스트 케이스만큼 반복
    N = int(input())                            # 양의 정수 개수 입력
    num_line = list(map(int, input().split()))  # 양의 정수 입력
    copied_list = num_line[:]                   # 양의 정수 리스트 복사
    for i in range(N-1, 0, -1):                 # 복사한 리스트 버블 정렬
        for j in range(0, i):
            if copied_list[j] > copied_list[j+1]:
                copied_list[j], copied_list[j+1] = copied_list[j+1], copied_list[j]
    min_value = copied_list[0]                  # 최솟값 저장
    max_value = copied_list[-1]                 # 최댓값 저장
    min_index = 0                               # 최솟값의 인덱스
    max_index = 0                               # 최댓값의 인덱스
    for i in range(N):                          # N만큼 반복
        if num_line[i] == min_value:            # 원래 리스트에서 최솟값에 해당하는 인덱스를 저장(앞에서 반복)
            min_index = i
            break
    for i in range(N-1, -1, -1):                # 원래 리스트에서 최댓값에 해당하는 인덱스를 저장(뒤에서 반복)
        if num_line[i] == max_value:
            max_index = i
            break
    answer = max_index - min_index              # 최댓값 - 최솟값
    if answer < 0:                              # 차가 음수이면
        answer = -answer                        # 음수부호 붙여주기
    print(f'#{test_case+1} {answer}')           # output 출력
