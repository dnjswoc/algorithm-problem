DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5

N = len(DATA)
TEMP = [0] * N

# 1단계 : DATA 원소 별 개수 세기
# DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
for x in DATA:
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):   # COUNT[1] ~ COUNT[4]까지 누적
    COUNTS[i] = COUNTS[i-1] + COUNTS[i]

# 3단계 : DATA의 맨 뒤부터 TEMP에 정렬
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1    # 누적개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]
print(TEMP)
