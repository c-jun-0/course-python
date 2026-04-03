"""
실습 15: 회원 할인 (삼항 연산자)

가격과 회원 여부(1: 회원, 0: 비회원)를 입력받아
회원이면 20% 할인, 비회원이면 5% 할인된 가격을 출력하세요.
삼항 연산자를 활용합니다.
"""

price = int(input("가격 입력: "))
is_member = int(input("회원 여부 (1: 회원, 0: 비회원): "))

# 아래에 삼항 연산자로 코드를 작성하세요

# 입력 받은 회원 여부로 회원이면 20% 할인 비회원이면 5% 할인된 가격 출력
# if is_member == 1:
#     print("최종가격: ",price - price * 0.2)
# else is_member == 0:
#     print("최종가격: ",price - price * 0.05)


# 삼항 연산자
discount_ratio = 0.2 if is_member == 1 else 0.05
price = int(price - price * discount_ratio)

result = print(f"최종가격: {price}")


"""
[실행 결과 예시] (입력: 10000, 1)
최종 가격: 8000원

[실행 결과 예시] (입력: 10000, 0)
최종 가격: 9500원
"""
