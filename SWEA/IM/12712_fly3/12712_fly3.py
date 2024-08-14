def onoff(numbers_switch, status, student_num, gen):
    for i in range(student_num):
        if gen[i][0] == 1:          # 남자
            for x,y in enumerate(numbers_switch):
                if y == gen[i][1]:  # 받은 카드랑 일치하는 번호
                    a = len(numbers_switch) // gen[i][1] # 존재하는 배수 개수
                    for z in range(1, a+1):
                        if status[z*y-1] == 1:  # 배수 개수 활용해서 1~배수개수 까지를 range로 정하고 뒤집기
                            status[z*y-1] = 0
                        else:
                            status[z*y-1] = 1
        else:       # 여자
            for c,v in enumerate(numbers_switch):
                if v == gen[i][1]:  # 받은 카드랑 일치하는 번호
                    w = 0
                    while status[c-w] == status[c+w]:   # 일치하는 인덱스에서 +- 양옆으로 가면서 일치할때 까지 w 늘리기
                        if c-w == 0 or c+w == len(numbers_switch)-1:
                            break
                        w += 1
                    if w > 0:       # w가
                        for l in range(2*w+1):
                            if status[c-w+l] == 1:
                                status[c - w + l] = 0
                            elif status[c-w+l] == 0:
                                status[c-w+l] = 1
                    elif w == 0:
                        if status[c] == 1:
                            status[c] = 0
                        else:
                            status[c] = 1
    return status

switch_N = int(input())
status = list(map(int,input().split()))
student_num = int(input())
gen = [list(map(int, input().split())) for _ in range(student_num)]
numbers_switch = []
for q in range(1, switch_N+1):
    numbers_switch.append(q)
answer = ' '.join(map(str,onoff(numbers_switch, status, student_num, gen)))
if len(answer) <= 40:
    print(answer[:39])
elif 80 > len(answer) > 40:
    print(answer[:39])
    print(answer[40:79])
elif 120 > len(answer) >= 80:
    print(answer[:39])
    print(answer[40:79])
    print(answer[80:119])
elif 160 > len(answer) >= 120:
    print(answer[:39])
    print(answer[40:79])
    print(answer[80:119])
    print(answer[120:159])
elif 200 >= len(answer) >= 160:
    print(answer[:39])
    print(answer[40:79])
    print(answer[80:119])
    print(answer[120:159])
    print(answer[160:200])


# 가람
def switch(total_switch, array, N, array_student):
    for i in range(N):
        # 남학생
        if array_student[i][0] == 1:
            for idx in range(1, (total_switch // array_student[i][1] + 1)):
                if array[array_student[i][1] * idx - 1] == 1:
                    array[array_student[i][1] * idx - 1] = 0
                elif array[array_student[i][1] * idx - 1] == 0:
                    array[array_student[i][1] * idx - 1] = 1
        # 여학생
        elif array_student[i][0] == 2:
            if array[array_student[i][1] - 2] != array[array_student[i][1]]:
                if array[array_student[i][1] - 1] == 1:
                    array[array_student[i][1] - 1] = 0
                elif array[array_student[i][1] - 1] == 0:
                    array[array_student[i][1] - 1] = 1
            # 양 옆이 대칭일 경우 +1칸 양 옆 대칭 확인 후 대칭이 안나올 때 까지 계속 +1
            else:
                cnt = 0
                for j in range(1,array_student[i][1] - 1):
                    if array[array_student[i][1] - 2 - j] == array[array_student[i][1] + j]:
                        cnt += 1
                    else:
                        break
                for idx in range(array_student[i][1] - 2 - cnt, array_student[i][1] + cnt +1):
                    if array[idx] == 0:
                        array[idx] = 1
                    elif array[idx] == 1:
                        array[idx] = 0

    return array




total_switch = int(input())
switch_status = list(map(int, input().split()))
total_student = int(input())
array_student = [list(map(int, input().split())) for _ in range(total_student)]

answer = switch(total_switch,switch_status,total_student, array_student)
for i in range(0, len(answer), 20):
    a = answer[i: i+20]
    print(*a)