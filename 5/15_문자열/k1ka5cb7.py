#튜플은 자바스크립트에서 const, final과 비슷하다고 생각하면 됨
# for : 언제까지 코드 짤지 아는 경우
# while :  그래프(stack 같은), 언제까지 쓸지 모를때

data = input()
result = [] 
sum = 0 

for x in data:
    # 알파벳일 때
    if x.isalpha():
        result.append(x)
    # 숫자면 더함
    else:
        sum += int(x) #정수 + 문자열을 더하면 에러가 뜨니까 int써줘야함 

# 알파벳 순서대로 정렬
result.sort()

# 숫자가 있었으면 더한 값을 result뒤에 붙이기
if sum != 0:
    result.append(str(sum))

#리스트를 문자열로 변환하여 출력
print(''.join(result))