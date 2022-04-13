travel_location = input("여행 장소를 입력해주세요: ")
travel_date = int(input("여행 일수를 입력해주세요: "))

if travel_location == "대전":
    travel_price = travel_date * 100000

elif travel_location == "부산":
    travel_price = travel_date * 150000

else:
    travel_price = 0

if travel_date >= 3:
    travel_price *= 0.9

elif travel_date < 0:
    travel_price = 0

if travel_price == 0:
    print("여행 장소나 여행 일수가 잘못 되었습니다.")

else:
    print("여행 경비는", str(int(travel_price)) + "원 입니다.")
