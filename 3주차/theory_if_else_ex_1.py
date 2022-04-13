print("해당 프로그램은 숫자를 입력하면, 해당 숫자가 정수형인지, 실수형인지 구분해주는 프로그램입니다.")

input_data = input("정수 또는 실수 데이터를 입력해주시길 바랍니다: ")

if str((int(float(input_data)))) == input_data:
  print("해당 데이터는 정수형 데이터가 맞습니다.")
 
else:
  print("해당 데이터는 정수형 데이터가 아닙니다.")
