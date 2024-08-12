T = int(input())                    # 테스트 케이스 입력


def list_sort(num_list, N):         # 리스트를 정렬할 함수 정의
    for i in range(N-1, 0, -1):     # 버블 정렬
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


for test_case in range(T):          # 테스트 케이스만큼 반복
    N = int(input())                # N : 입력 받을 숫자 개수
    num_list = list(map(int, input().split()))  # N개의 숫자 입력
    num_list = list_sort(num_list, N)       # 함수 호출
    print(f'#{test_case+1} {" ".join(map(str, num_list))}')     # output 출력
