import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 16진수에서 A ~ F까지의 경우를 10진수 수로 바꾸기 위한 딕셔너리
hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def tree(num):  # 중위순회 순서를 기록하기 위한 함수
    if num > 8:
        return
    tree(num * 2)
    inorder_seq.append(num)
    tree(num * 2 + 1)


for test_case in range(T):
    password = list(input())
    N = int(password[0])
    node_lst = []   # 16진수를 10진수로 바꾸고 노드로 저장할 리스트
    inorder_seq = []    # 중위순회 시 완전 이진 트리가 루트노드부터 기록되는 순서
    dec = 0     # 16진수를 10진수로 변환할 변수
    answer = ''  # 정답을 기록할 빈 문자열 생성

    for i in range(1, 17):  # 입력받은 password 리스트의 1번 인덱스부터 16번 인덱스까지 암호문자열이 있기 때문에
        if password[i].isdecimal(): # 0 ~ 9까지면 정수형으로 변환
            password[i] = int(password[i])
        elif password[i] in hex_dict:   # 16진수 딕셔너리에 존재하면 그에 맞는 정수로 변환
            password[i] = hex_dict[password[i]]
        if i % 2 == 1:  # 홀수 인덱스는 16을 곱해준다
            password[i] *= 16
        dec += password[i]  # 전처리한 값들을 더해준다
        if i % 2 == 0:  # 짝수 인덱스라면
            dec -= N * i//2  # 다음 16진수 수로 새로 시작해야하므로 더한 값에서 salt 값을 빼고
            if dec >= 10:   # 10보다 크면 1의 자리 수만 노드에 기록하므로 10으로 나눈 나머지로 기록
                dec %= 10
            node_lst.append(dec)    # 결과값을 node_lst에 저장
            dec = 0

    tree(1)  # 1부터 시작해서 8까지 완전 이진 트리의 중위 순회 순서를 기록

    for i in range(1, 9):   # 1번부터 8번 순서까지 해당하는 노드를 찾기 위해서
        for j in range(8):
            if inorder_seq[j] == i:  # 중위순회 순서에 해당하는 인덱스를 골라
                answer += str(node_lst[j])  # 그 인덱스를 노드 리스트에 대입하여 답을 구한다.
    print(f'#{test_case + 1} {answer}')
