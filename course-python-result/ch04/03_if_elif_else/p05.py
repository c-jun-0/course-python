"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 5: BMI 판정

키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하고 판정 결과를 출력하세요.
if/elif/else를 사용합니다.

BMI = 몸무게(kg) / (키(m))^2
(키는 cm로 입력받으므로 m로 변환 필요: cm / 100)

[판정 기준]
BMI 18.5 미만: 저체중
BMI 18.5 이상 23 미만: 정상
BMI 23 이상 25 미만: 과체중
BMI 25 이상: 비만
"""

height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# 아래에 BMI를 계산하고 판정 결과를 출력하세요

# 키, 몸무게 출력
print(f"키: {height}cm, 몸무게: {weight}kg")

# BMI = 몸무게 / 키 ** 2
BMI = weight / (height / 100) ** 2
# BMI 출력
print(f"BMI: {BMI:.2f}")

# BMI 판정 값 출력
# BMI 값이 18.5 미만: 저체중
if BMI < 18.5:
    print("판정: 저체중")
# BMI 값이 18.5 이상 23 미만: 정상
elif BMI < 23:
    print("판정: 정상")
# BMI 값이 23이상 25미만: 과체중
elif BMI < 25:
    print("판정: 과체중")
# BMI 값이 25 이상: 비만
else:
    print("판정: 비만")


"""
[실행 결과 예시] (입력: 170, 65)
키: 170.0cm, 몸무게: 65.0kg
BMI: 22.49
판정: 정상
"""
