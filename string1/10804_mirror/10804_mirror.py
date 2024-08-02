T = int(input())                        # 테스트 케이스 입력


def mirror_str(string_list, num):       # 리스트의 맞은 편의 인덱스만 바꾸는 함수
    for i in range(num//2):             # 리스트 길이의 몫만큼 반복
        string_list[i], string_list[-(i+1)] = string_list[-(i+1)], string_list[i]   # 맞은 편 인덱스의 값을 서로 바꿈
    return string_list                  # 바꾼 리스트 반환


def change_str(string_list, num):       # 바꾼 리스트에서 문자열을 거울에 비치는 모습으로 뒤집는 함수
    for i in range(num):                # 리스트 길이만큼 반복
        if string_list[i] == 'b':       # b는 d로
            string_list[i] = 'd'
        elif string_list[i] == 'd':     # d는 b로
            string_list[i] = 'b'
        elif string_list[i] == 'p':     # p는 q로
            string_list[i] = 'q'
        else:                           # 나머지는 p로 변경
            string_list[i] = 'p'
    return string_list                  # 변경한 리스트 반환


for test_case in range(T):              # 테스트 케이스만큼 반복
    str_list = list(input())            # string 입력 후 리스트로 변환
    count = 0                           # 리스트 길이 개수
    for str_1 in str_list:              # 리스트 길이 개수 계산
        count += 1
    new_list = mirror_str(str_list, count)  # 리스트의 맞은 편 인덱스끼리 바꾸는 함수 호출
    new_mirror_list = change_str(new_list, count)   # 문자열을 반대 모습으로 바꾸는 함수 호출
    print(f'#{test_case+1}', end=" ")   # output 출력
    for chr_1 in new_mirror_list:
        print(chr_1, end='')
    print()
