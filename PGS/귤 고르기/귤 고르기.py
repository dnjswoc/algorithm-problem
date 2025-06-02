'''
귤을 k개 고를 때 크기가 다른 그룹의 수를 최소화하기

ex.
k = 6, tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
selected_tangerine = [2, 2, 3, 3, 5, 5]
result = 3 (2, 3, 5)

귤 크기 집단을 내림차순하여 가장 많은 것부터 차감하면서 k를 다 채우면 끝내야겠다고 생각
'''

def solution(k, tangerine):
    
    # 크기 집단 별로 개수를 구하기 위해 0 리스트 생성
    count = [0] * max(tangerine)
    
    for i in tangerine:
        # 집단 별 개수 세기
        count[i-1] += 1
        
    # 가장 많은 집단부터 내림차순 정렬
    count.sort(reverse=True)
    
    answer = 0
    
    for j in count:
        # 가장 많은 집단부터 k개 다 채우도록 계산
        k -= j
        # 집단 하나 끝날 때마다 count 추가
        answer += 1

        # k를 다 채우면 반복문 탈출
        if k <= 0:
            break

    print(answer)
    return answer