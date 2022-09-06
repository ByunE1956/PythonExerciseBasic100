# 기초 산술연산 문제

# 문제1 - 정수 1개 입력받아 부호바꾸기
n = int(input())
print(-n)

# 문제2 - 문자 1개 입력받아 다음 문자 출력하기
n = ord(input())
print(chr(n+1))

# 문제3 - 정수 2개 입력받아 차 계산하기
a, b = input().split()
c = int(a) - int(b)
print(c)

# 문제4 - 실수 2개 입력받아 곱 계산하기
a, b = input().split()
c = float(a) * float(b)
print(c)

# 문제5 - 단어 여러 번 출력하기
w, n = input().split()
print(w * int(n))

# 문제6 - 문장 여러 번 출력하기
n = int(input())
s = input()
print(n * s)

# 문제7 - 정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
c = int(a) ** int(b)
print(c)

# 문제8 - 실수 2개 입력받아 거듭제곱 계산하기
f1, f2 = input().split()
c = float(f1) ** float(f2)
print(c)

# 문제9 - 정수 2개 입력받아 나눈 몫 계산하기
a, b = input().split()
a, b = int(a), int(b)
print(a//b)

# 문제10 - 정수 2개 입력받아 나눈 나머지 계산하기
a, b = input().split()
print(int(a) % int(b))

# 문제11 - 실수 2개 입력받아 나눈 결과 계산하기
f1, f2 = input().split()
c = float(f1) / float(f2)
print(format(c, ".3f"))

# 문제12 - 정수 2개 입력받아 자동 계산하기
a, b = input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format((float(a) / float(b)), ".2f"))
#print(round(a/b, 2)) : round => 반올림 함수 But, 주의할 점이 반올림에 대해 정확하진 않음 1.5 => 2, 2.5 => 2 둘 다 2가 반환됨

# 문제13 - 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
d = int(a) + int(b) + int(c)
e = d / 3
print(d, format(e, ".2f"))

'''
python 프로그래밍을 처음 배울 때 좋은 습관(단계)
1. 입력된 문자열을 정확하게 잘라낸다.(공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)
2. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. (정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)
3. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 변수를 이용해 계산을 한다.
4. 원하는 결과 값을 필요한 형태로 만들어 출력한다.(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)
'''