from collections import deque 
def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    maximum = max(priorities)

    print(maximum) #3
    answer = 0
    while True:
        index = index_list.popleft() #왼쪽 값을 빼서 index에 넣고  
        if priorities[index] < maximum: #만약 우선순위 index번째의 값이 3보다 작으면
            index_list.append(index) # 뺀 값을 뒤에 넣어줌
        else:
            #우선순위 index번째 값이 3이면
            answer += 1
            priorities[index] = 0
            maximum = max(priorities) #2
            if index == location:
                return answer

solution([2, 1, 3, 2], 2)