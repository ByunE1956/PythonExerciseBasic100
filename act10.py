# 기초 조건/선택실행구조

# 문제1 - 정수 3개 입력받아 짝수만 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 문제2 - 정수 3개 입력받아 짝/홀 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")

# 문제3 - 정수 1개 입력받아 분류하기
a = int(input())
if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

# 문제4 - 점수 입력받아 평가 출력하기
a = int(input())
if a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 문제5 - 평가 입력받아 다르게 출력하기
a = input()
if str.upper(a) == 'A':
    print('Best!!!')
elif str.upper(a) == 'B':
    print('Good!!')
elif str.upper(a) == 'C':
    print('Run!')
elif str.upper(a) == 'D':
    print('Slowly~')
else:
    print("What???")

# 문제6 - 월 입력받아 계절 출력하기
a = int(input())
if a//3 == 1:
    print("spring")
elif a//3 == 2:
    print("summer")
elif a//3 == 3:
    print("fall")
else:
    print("winter")