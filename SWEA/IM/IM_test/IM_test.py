'''
input sample들을 봤을 때 1부터 숫자가 커지면서 전구의 불을 바뀌면
그 이후에는 숫자가 커지면서 이전의 숫자는 다른 숫자의 배수가 될 수 없으므로 1부터 불을 바꾸어 나가야겠다고 생각했습니다.
그렇게 생각하고 문제를 풀었더니 풀렸습니다ㅎㅎ
'''


T = int(input())

for test_case in range(T):
    N = int(input())
    light_arr = list(map(int, input().split()))     # 입력받은 전구의 상태
    start_arr = [0] * N     # 초기 전구의 상태(불이 다 꺼져있음)
    switch_cnt = 0  # 스위치를 누르는 단계 수
    while start_arr != light_arr:   # 입력받은 전구의 상태와 같아질 때까지
        for i in range(N):
            if start_arr[i] != light_arr[i]:    # 입력받은 전구의 상태와 달라지는 첫 번째 인덱스
                idx = i
                break
        times = N // (idx + 1)  # 배수의 개수(바꿔야 하는 스위치 개수)
        for time in range(1, times + 1):    # 인덱스의 배수만큼 반복하며 스위치 상태 변경
            if start_arr[((idx + 1) * time) - 1]:
                start_arr[((idx + 1) * time) - 1] = 0
            else:
                start_arr[((idx + 1) * time) - 1] = 1
        switch_cnt += 1
    print(f'#{test_case + 1} {switch_cnt}')
