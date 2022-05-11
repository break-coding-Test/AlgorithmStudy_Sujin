import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    dataArr = input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환
    arr.append((dataArr[0], int(dataArr[1])))   

#key로 점수기준으로 재정렬
arr = sorted(arr, key=lambda student : student[1])

for student in arr:
    print(student[0], end=' ')