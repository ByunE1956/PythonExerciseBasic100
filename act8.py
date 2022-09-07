# 기초 논리연산

#문제1 - 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

#문제2 - 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

#문제3 - 둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#문제4 - 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#문제5 - 참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))

#문제6 - 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((not a and not b) or (a and b))

#문제7 - 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not(a or b))