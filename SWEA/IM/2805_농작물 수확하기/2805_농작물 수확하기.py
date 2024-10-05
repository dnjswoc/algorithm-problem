import sys
sys.stdin = open('input.txt')

T = int(input())                    # 테스트 케이스 입력


def farm(arr, num):                 # 농작물 수확량 계산하는 함수 정의
    row = 0                         # 행 0으로 초기화
    col = num//2                    # 열은 N//2로 기준을 잡는다.
    k = 0                           # 행을 반복하며 k를 늘리고 줄여 농작물 수확량 계산
    total_sum = 0                   # 총 농작물 수확량을 저장할 변수
    dj = [1, -1]                    # 열에 대한 델타 탐색
    while row < num:                # 행을 0부터 N-1까지 반복
        farm_sum = arr[row][col]    # 반복하는 행의 농작물의 초깃값은 기준으로 삼은 N//2 열의 값으로 설정한다.
        for delta in dj:            # 위에서 설정한 기준값으로부터 델타 탐색하여 농작물을 더해준다
            if k == 0: continue     # k == 0의 경우는 continue
            for i in range(1, k+1):  # i를 1부터 k+1까지 반복
                farm_sum += arr[row][col + delta*i]  # 델타 탐색을 통해 행의 농작물 수확량을 더해준다.
        total_sum += farm_sum       # 총 농작물 수확량에 행의 농작물 수확량을 더해준다
        if row < col:               # 행이 열의 기준값 N//2까지는
            k += 1                  # k를 1씩 증가시키고
        else:                       # 행이 열의 기준값 N//2를 넘어서면
            k -= 1                  # k를 1씩 감소시킨다
        row += 1                    # 행을 1씩 증가
    return total_sum                # 총 농작물 수확량을 return


for test_case in range(T):
    N = int(input())                # 정방행렬의 행의 개수
    farm_arr = [list(map(int, input())) for _ in range(N)]  # 정방행렬 입력
    answer = farm(farm_arr, N)      # 총 농작물 수확량을 계산하는 함수 호출
    print(f'#{test_case+1} {answer}')   # output 출력

