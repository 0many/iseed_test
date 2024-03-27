## 4
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("장학생", end='')
elif score >= 60:
    print("합격", end='')
else:
    print("불합격", end='')

print("입니다. ^^")

## 5
num = 5
if num % 2 == 0:
    res = '짝수'
else:
    res = '홀수'
print(res)
# =====
num = 5
res = '짝수' if num % 2 == 0 else '홀수'
print(res)

## 6
nn = [100, 200, 300, 400, 500]
# 6-1
[100, 777, 300, 400, 500]
# 6-2
[100, [444, 555], 300, 400, 500]
# 6-3
[100, 444, 555, 500]
# 6-4
[100, 200]

## 8
hap = 0
n = 1234

while n < 4568:
    if n % 444 == 0:
        hap += n
    n += 1

print(hap)

## 9
sum = 0

for n in range(3333, 10000):
    if n % 1234 == 0:
        if sum + n > 100000:
            break
        sum += n
    else:
        continue

## 14
myData = [[n * m for n in range(1, 3)] for m in range(2, 4)]
print(myData)

## 5
nn = [100, 200, 300, 400, 500]
print(nn[4])
print(nn[-1])
print(nn[-2])
print(nn[1:4])
print(nn[0:1])
print(nn[2:-1])
print(nn[0::2])
print(nn[::-1])
print(nn[::-2])







