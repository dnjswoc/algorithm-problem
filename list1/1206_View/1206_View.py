T = 10					# 테스트 케이스 10개

for i in range(1, T+1):			# 1부터 10까지 반복
    N = int(input())		   	 # 건물 개수 입력
    sum_building = 0		  # 조망권 칸 개수
    test_case = list(map(int, input().split()))			# 건물 높이 입력
    for tc in range(2, N-2):
        test_case_sort = test_case[tc-2:tc+3]		 # 길이가 5인 리스트 추출(정렬 시 사용)
        test_case_list = test_case[tc-2:tc+3]		  # 길이가 5인 리스트 추출(값 비교 시 사용)
        max_case_list = []
        for j in range(4, 1, -1):						  # 길이가 5인 리스트 정렬하는 반복문
            for k in range(j):
                if test_case_sort[k] > test_case_sort[k+1]:
                    test_case_sort[k], test_case_sort[k+1] = test_case_sort[k+1], test_case_sort[k]
        max_case_list = test_case_sort[3:]			# 가장 큰 값과 그 다음으로 큰 값을 리스트에 삽입
        max_tc = max_case_list[-1]					# 최댓값
        if test_case_list[2] == max_tc:				  # 리스트 가운데 값이 최댓값과 같으면 그 다음으로 큰 값을 뺀다.
            answer = test_case_list[2] - max_case_list[0]
            sum_building += answer				  # answer(조망권 칸) 더하기

    print(f'#{i} {sum_building}')