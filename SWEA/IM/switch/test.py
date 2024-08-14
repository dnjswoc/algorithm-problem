import sys
sys.stdin = open('input.txt')

N = int(input())        # 스위치 개수
switch_arr = list(map(int, input().split()))    # 스위치 상태
students = int(input())  # 학생 수 입력
student_information = [list(map(int, input().split())) for _ in range(students)]    # 학생 정보
for student in student_information:  # 학생 한 명의 정보를 가져와서
    if student[0] == 1:         # 남학생이면
        num = N // student[1]
        for i in range(1, num + 1):
            if switch_arr[(student[1] * i) - 1]:    # 학생이 받은 번호의 배수일 때의 스위치 상태 바꾸기
                switch_arr[(student[1] * i) - 1] = 0
                continue
            switch_arr[(student[1] * i) - 1] = 1
        continue
    j = 0       # 여학생이면
    standard_idx = student[1] - 1   # 학생이 받은 번호에서부터의 스위치 대칭을 확인
    while switch_arr[standard_idx - j] == switch_arr[standard_idx + j]:  # 대칭이면 스위치 상태 변경
        if switch_arr[standard_idx - j]:
            switch_arr[standard_idx - j], switch_arr[standard_idx + j] = 0, 0
        else:
            switch_arr[standard_idx - j], switch_arr[standard_idx + j] = 1, 1
        j += 1
        if standard_idx - j < 0 or standard_idx + j > N - 1:   # 인덱스 범위 넘어가면 반복문 종료
            break

for k in range(len(switch_arr)):
    if k % 20 == 0 and k != 0:
        print()
    print(switch_arr[k], end=' ')
