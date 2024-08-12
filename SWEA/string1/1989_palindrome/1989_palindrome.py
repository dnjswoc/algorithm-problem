T = int(input())                        # 테스트 케이스 입력


def mirror_str(string_list, num):       # 리스트의 맞은 편 인덱스끼리 교환하는 함수
    for i in range(num//2):
        string_list[i], string_list[-(i+1)] = string_list[-(i+1)], string_list[i]
    return string_list                  # 변경된 리스트 반환


def check_str(string_list, new_string_list):    # 원래 리스트와 변경된 리스트가 같은지 확인하는 함수
    if string_list == new_string_list:
        return 1                                # 같으면 1 반환
    else:
        return 0                                # 다르면 0 반환


for test_case in range(T):              # 테스트 케이스만큼 반복
    str_list = list(input())            # 문자열 입력
    original_list = str_list[:]         # 인덱싱으로 원래 문자열 복사
    count = 0                           # 리스트 개수 변수
    for str_1 in str_list:              # 리스트 개수 계산
        count += 1
    new_list = mirror_str(str_list, count)  # 리스트의 맞은 편 인덱스끼리 교환하는 함수 호출
    answer = check_str(original_list, new_list)  # 원래 리스트와 변경된 리스트가 같은지 확인하는 함수 호출 
    print(f'#{test_case+1} {answer}')   # output 출력
