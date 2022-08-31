# 기초 값변환 문제

# 문제1 - 16진 정수 입력받아 8진수로 출력하기
#a = int(input(), 16)
#print("%o" %a)

# 문제2 - 영문자 1개 입력받아 10진수로 변환하기
a = ord(input())
print(a)

# 문제3 - 정수 입력받아 유니코드 문자로 변환하기
a = int(input())
print(chr(a))

# 문제4 - 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f"))