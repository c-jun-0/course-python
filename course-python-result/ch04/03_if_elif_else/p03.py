"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 3: 교통수단 추천

거리(km)를 입력받아 적절한 교통수단을 추천하세요.
if/elif/else를 사용합니다.

[추천 기준]
2km 미만: 도보
2km 이상 5km 미만: 자전거
5km 이상 20km 미만: 버스
20km 이상: 지하철
"""

distance = float(input("거리를 입력하세요 (km): "))
print(f"거리: {distance}km")

# 아래에 교통수단을 추천하여 출력하세요

# 입력 받은 값에서 2km 미만이면 도보
if distance < 2:
    print("추천 교통수단: 도보")
# 2km 이상 5km 미만이면 자전거
elif distance < 5:
    print("추천 교통수단: 자전거")
# 5km 이상 20km 미만이면 버스
elif distance < 20:
    print("추천 교통수단: 버스")
# 20km 이상이면 지하철
else:
    print("추천 교통수단: 지하철")



"""
[실행 결과 예시] (입력: 8.5)
거리: 8.5km
추천 교통수단: 버스
"""
