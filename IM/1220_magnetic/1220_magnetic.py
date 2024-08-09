import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(10):
    arr_size = int(input())             # 행렬 크기 입력
    magnetic_arr = [list(map(int, input().split())) for _ in range(arr_size)]   # 행렬 입력
    agglutination = 0                   # 교착 상태 개수를 세기 위한 변수
    for col in range(arr_size):         # 열 반복
        check_agglutination = []        # 열에 존재하는 1과 2를 순서대로 저장하기 위해 리스트 생성 
        for row in range(arr_size):     # 행 반복
            if magnetic_arr[row][col] > 0:  # 행렬 값이 0 초과면
                check_agglutination.append(magnetic_arr[row][col])  # 리스트에 저장
        for mg in range(len(check_agglutination)-1):    # 리스트 개수 -1 만큼 반복
            if check_agglutination[mg] == 1 and check_agglutination[mg + 1] == 2:   # 1과 2가 순서대로 붙어 존재하면
                agglutination += 1      # 교착 상태 개수 1씩 증가
    print(f'#{test_case+1} {agglutination}')    # output 출력
