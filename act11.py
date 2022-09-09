# 기초 반복실행구조

# 문제1 - 0입력될 때까지 무한 출력하기
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

# 문제2 - 정수 1개 입력받아 카운트다운 출력하기1
n = int(input())
while n != 0:
    print(n)
    n -= 1

# 문제3 - 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())
while n != 0:
    n -= 1
    print(n)

# 문제4 - 문자 1개 입력받아 알파벳 출력하기
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end=' ')
    t += 1

# 문제5 - 정수 1개 입력받아 그 수까지 출력하기1
n = int(input())
t = 0
while t <= n:
    print(t)
    t += 1

# 문제6 - 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())
for i in range(n+1):
    print(i)