# 기초 비트단위논리연산

# 문제1 - 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

# 문제2 - 비트단위로 AND 하여 출력하기
a, b = input().split()
print(int(a) & int(b))

# 문제3 - 비트단위로 OR 하여 출력하기
a, b = input().split()
print(int(a) | int(b))

# 문제4 - 비트단위로 XOR 하여 출력하기
a, b = input().split()
print(int(a) ^ int(b))


# 기초 3항연산

# 문제1 - 정수 2개 입력받아 큰 값 출력하기
a, b = input().split()
a = int(a)
b = int(b)
print(a if(a >= b) else b)

# 문제2 - 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a if a<b else b) if ((a if a<b else b)<c) else c)