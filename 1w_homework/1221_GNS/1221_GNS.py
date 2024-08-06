# import sys
# sys.stdin = open('input.txt')

T = int(input())                                # 테스트 케이스 입력

for test_case in range(T):                      # 테스트 케이스만큼 반복
    test_case_num, chr_num = input().split()    # 조건 입력
    chr_num = int(chr_num)                      # 정수형으로 변환
    num_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}  # 딕셔너리 초기화
    num_list = list(input().split())            # 문제 입력
    for num in num_list:                        # 입력된 리스트의 요소 반복
        if num in num_dict.keys():              # 해당 요소가 딕셔너리의 키와 같으면
            num_dict[num] += 1                  # 그 키에 해당하는 값에 1 증가
    num_chr_list = []                           # 숫자를 다시 글자로 변환하여 출력할 리스트 생성
    for num_chr, num_int in num_dict.items():   # 딕녀서리의 키-값 순회
        num_chr_list += [num_chr] * num_int     # 키와 그에 해당하는 값만큼 키를 리스트에 저장
    print(f'#{test_case+1}')                    # output 출력
    for i in range(chr_num):
        print(num_chr_list[i], end=' ')
    print()
