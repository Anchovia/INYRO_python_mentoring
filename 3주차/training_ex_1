Temp = float(input("섭씨 기온을 입력해주세요: "))
Humid = float(input("상대 습도를 입력해주세요: "))

DI = 0.81 * Temp + 0.01 * Humid * (0.99 * Temp - 14.3) + 46.3

if DI < 70:
    print("쾌적합니다.")

elif DI >= 70 and DI < 80:
    print("일부 사람들이 불쾌감을 느낄 수 있습니다.")

elif DI >= 80 and DI <= 83:
    print("50%정도의 사람들이 불쾌감을 느낍니다.")

else:
    print("대부분의 사람들이 불쾌감을 느낍니다.")
