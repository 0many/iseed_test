## 5
ss = "Python"

for i in range(0, len(ss)):
    print(ss[i] + "$", end = "")

## 9
inStr, outStr = "python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[strLen - i - 1]

print("내용을 거꾸로 출력 --> %s " % outStr)

## 11
import re
str = "파이썬###CookBook$$$@@@열공중1234"
result = re.sub(r'[^가-힣a-zA-Z\s]', "", str)
print(result)

## 13
import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20
radius, angle, radian = 200, 0, 0

## 메인 코드 부분 ##
turtle.shape('turtle')
turtle.setup(width = swidth + 100, height = sheight + 100)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360 / len(inStr)

for ch in inStr :
    radian = 3.14*angle/180

    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize,  'bold'))

    angle += 360 / len(inStr)

turtle.done()

## 3
def plus(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = plus(100, 200,300)
print(hap)

## 4
def f1():
    print(var)

def f2():
    var = 10
    print(var)

var = 100
f1()
f2()

## 8
def myFunc(p1=1, p2=2, p3=3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 =>", myFunc())
print("매개변수가 1개로 호출 ==>", myFunc(1))
print("매개변수가 2개로 호출 ==> ", myFunc(1, 2))
print("매개변수가 3개로 호출 ==>", myFunc(1, 2, 3))


## 11
def addNumber(num):
    if num == 1:
        return 1
    else:
        return num + addNumber(num-1)
print(addNumber(100))







