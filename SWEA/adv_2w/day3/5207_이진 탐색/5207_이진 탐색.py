import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    cnt = 0
    a_lst = sorted(a_lst)

    for b in b_lst:  # 리스트 B 원소 하나씩 순회
        l, r = 0, N - 1  # l, r의 시작을 각각 0번째 인덱스, 마지막 인덱스 번호로 설정
        m = (l + r) // 2
        l_lst = [l]
        r_lst = [r]
        while True:
            if len(l_lst) >= 3:
                # 세 번 연속으로 같은 l이나 r을 가지면 연속으로 같은 방향을 가진다고 본다.
                if l_lst[-1] == l_lst[-3] or r_lst[-1] == r_lst[-3]:
                    break
            if b == a_lst[m]:   # m번 째 리스트 값과 일치하면 cnt + 1
                cnt += 1
                break
            if b > a_lst[m]:    # 탐색할 값이 m번 째 리스트 값보다 크면
                l = m + 1
                l_lst.append(l)
                r_lst.append(r)
                m = (l + r) // 2
                continue
            else:               # 탐색할 값이 m번 째 리스트 값보다 작으면
                r = m - 1
                l_lst.append(l)
                r_lst.append(r)
                m = (l + r) // 2
                continue
    print(f'#{test_case} {cnt}')
