T = int(input())                        # 테스트 케이스 입력


def list_sort(num_list):                # 버블 정렬로 입력 받은 리스트 정렬
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


def special_sort(num_list, list_len):   # 특별한 정렬 시행
    special_list = [0] * 10             # 길이가 10인 리스트 생성
    for i in range(10):                 # 10만큼 반복
        if i % 2 == 0:                  # i가 짝수이면
            special_list[i] = num_list[list_len-int((i+2)/2)]   # 짝수 인덱스에 최댓값부터 저장
        elif i % 2 != 0:                # i가 홀수이면
            special_list[i] = num_list[int((i-1)/2)]            # 홀수 인덱스에 최솟값부터 저장
    return special_list


for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 리스트 크기 입력
    arr = list(map(int, input().split()))   # 리스트 입력
    new_arr = list_sort(arr)            # 버블 정렬 함수 호출
    special_sorted_list = special_sort(new_arr, N)  # 특별한 정렬 함수 호출
    print(f'#{test_case+1}', end=' ')   # output 출력
    for num in special_sorted_list:
        print(num, end=' ')
    print()

