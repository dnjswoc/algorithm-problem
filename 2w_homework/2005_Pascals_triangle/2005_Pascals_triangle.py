import sys
sys.stdin = open('input.txt')

T = int(input())


def pascal_triangle(num):                           # 파스칼 삼각형 구하는 함수
    pas_tri = [[0] * i for i in range(1, num+1)]    # 0으로 구성된 2차원 배열 생성
    pas_tri[0][0] = 1                               # 맨 위 꼭짓점은 1
    for i in range(1, num):                         # 1부터 주어진 숫자-1까지 반복
        for j in range(i+1):                        # 0부터 i+1까지 반복
            if i == 1:                              # 삼각형 2번째은 [1, 1]
                pas_tri[i][j] = 1
            elif i > 1:                                 # 세번째 줄부터
                pas_tri[i][0], pas_tri[i][-1] = 1, 1    # 양 끝은 1로 설정
                if 1 <= j < i:                          # 중간 값은
                    pas_tri[i][j] = pas_tri[i-1][j-1] + pas_tri[i-1][j]  # 윗 줄 양쪽 값 더해서 구한다.
    return pas_tri


for test_case in range(T):
    N = int(input())
    answer_list = pascal_triangle(N)
    print(f'#{test_case+1}')
    for i in range(N):
        for j in range(i+1):
            print(answer_list[i][j], end=' ')
        print()
