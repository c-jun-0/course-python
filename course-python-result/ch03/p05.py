"""
실습 5: BMI 계산기

키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하세요.

BMI 공식: 몸무게(kg) / 키(m)의 제곱
주의: 키는 cm로 입력받지만, 공식에서는 m 단위를 사용합니다.

힌트: cm → m 변환은 / 100, 제곱은 ** 2를 사용합니다.
"""

height = int(input("키(cm)를 입력하세요: "))
weight = int(input("몸무게(kg)를 입력하세요: "))

# 아래에 BMI를 계산하여 출력하세요

# cm -> m로 변환
height = height / 100
# 키의 제곱
height = height ** 2
# BMI 계산하기
BMI = weight / height
# 계산한 BMI 출력
print(f"BMI: {BMI}")


"""
[실행 결과 예시] (입력: 175, 70)
키: 175cm
몸무게: 70kg
BMI: 22.857142857142858
"""