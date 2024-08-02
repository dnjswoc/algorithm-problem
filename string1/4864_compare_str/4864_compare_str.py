T = int(input())                    # 테스트 케이스 입력

for test_case in range(T):          # 테스트 케이스만큼 반복
    str_1 = input()                 # str1 입력
    str_2 = input()                 # str2 입력
    N = 0                           # str1의 개수
    M = 0                           # str2의 개수
    string_part_list = []           # str2의 부분들을 저장할 리스트
    for str_chr in str_1:           # str1의 개수 계산
        N += 1
    for str_chr in str_2:           # str2의 개수 계산
        M += 1
    for i in range(M - N + 1):      # M - N + 1만큼 반복
        string_part_list += [str_2[0 + i:N + i]]    # N 만큼의 크기의 윈도우를 만들어 str2에서 움직여 나오는 값을 리스트에 저장
    if str_1 in string_part_list:   # 윈도우를 통해 나온 리스트에 str1이 존재하면
        print(f'#{test_case+1} 1')  # 1 출력
    else:
        print(f'#{test_case+1} 0')  # 아니면 0 출력
