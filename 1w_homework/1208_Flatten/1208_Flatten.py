T = 10                                  # 테스트 케이스


def bubble_sort(boxes):                 # 버블 정렬하는 함수
    for i in range(99, -1, -1):
        for j in range(0, i):
            if boxes[j] > boxes[j+1]:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
    return boxes                        # 정렬된 함수 return


def dump_box(boxes, dumps):             # 정렬된 함수에서 덤프하는 함수
    for dump in range(dumps):           # 덤프 횟수만큼 반복
        boxes[-1] -= 1                  # 정렬된 함수의 마지막 인덱스 값에 -1
        boxes[0] += 1                   # 정렬된 함수에서 첫번째 인덱스 값에 +1
        boxes = bubble_sort(boxes)      # 변경된 값이 있어 다시 버블 정렬
    return boxes                        # 덤프 횟수 반복 후 정렬하고 return


for test_case in range(T):              # 테스트 케이스만큼 반복
    D = int(input())                    # 덤프 입력
    box_list = list(map(int, input().split()))  # 박스 높이 입력
    sorted_box = bubble_sort(box_list)  # 버블 정렬 함수 호출
    new_box = dump_box(sorted_box, D)   # 덤프 함수 호출
    answer = new_box[-1] - new_box[0]   # 덤프 후 마지막 인덱스 - 첫번째 인덱스
    print(f'#{test_case+1} {answer}')   # output 출력
