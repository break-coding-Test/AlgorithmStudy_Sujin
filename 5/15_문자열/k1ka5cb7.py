String = input()
result = []
sum = 0

for x in String:
    # 알파벳일 때
    if x.isalpha():
        result.append(x)
    # 숫자면 더함
    else:
        sum += int(x)

# 알파벳 순서대로 정렬
result.sort()

# 숫자가 있었으면 더한 값을 result뒤에 붙이기
if sum != 0:
    result.append(str(sum))

#리스트를 문자열로 변환하여 출력
print(''.join(result))