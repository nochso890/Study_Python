# 자료형

# 숫자
print(5)
print(-10)
print(5 - 10)
print(3.10)
print(3.14 * 3)

# 문자
print("큰따옴표")
print('작은따옴표')
print("   공백")
print(" " * 4 + "공백")

version = 3.10
beginner = "기초과정"
year = 2022
month = 8
day = 22

print("파이썬" + str(version) + "으로 시작함")
print("이제", beginner, "을", "시작함")  # ,의 경우 띄어 쓰기
print(str(year) + "." + str(month) + "." + str(day))

# 참 / 거짓
print(6 > 7)
print(5 == 5)
print(6 <= 8)
print("ABC" == "abc")
print("ABC" == "ABC")

print(not (1 <= 2))
print(not (1 != 3))
print((3 > 0) and (4 < 5))
print((3 > 0) or (4 < 5))
print((3 > 0) | (4 < 5))
print((3 > 0) & (4 < 5))

# 문제
station = ["사당", "신도림", "인천공항"]

print(station.__getitem__(0) + "행 열차가 들어오고 있습니다.")
print(station.__getitem__(1) + "행 열차가 들어오고 있습니다.")
print(station.__getitem__(2) + "행 열차가 들어오고 있습니다.")

# 연산
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2 ** 3)  # 제곱
print(5 % 3)
print(10 % 3)
print(10 // 3)  # 목을 구하기

# 숫자처리함수
print(abs(-5))  # 절대값
print(pow(4, 2))  # 승수
print(max(4, 15))  # 최대값 반환
print(min(3, 20))  # 최소값 반환
print(round(3.145))  # 반올림

from random import *

offlineDate = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(offlineDate) + " 일로 선정되었습니다.")

# 문자열
sentence = '파이썬 스터디'
print(sentence)
sentence2 = "공부하는중 입니다."
print(sentence2)
sentence3 = """ 파이썬 을 
오늘부터 공부
하고 있습니다."""
print(sentence3)

# 슬라이싱
identityNum = "123456-1234567"

gender = "남" if identityNum[7] != 1 else "여"
year = identityNum[0:2]
month = identityNum[2:4]
day = identityNum[4:6]

print("성별 : " + str(gender))
print("연 : " + year)
print("월 : " + month)
print("일 : " + day)
