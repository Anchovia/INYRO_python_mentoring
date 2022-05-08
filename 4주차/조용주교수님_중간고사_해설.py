# 이니로_파이썬_조용주교수님_중간고사_해설_병훈.py
# carolsuki7

# 윤년 처리 함수
# 윤년: 서력기원의 연수가 4로 나누어 떨어지는 해 ex) 2000년, 2004년, ...
def leap_year_convert_func(int_year):
    # 윤년일 때
    if int_year % 4 == 0:
        return True

    # 윤년이 아닐때
    else:
        return False

# 년도 변환 함수
def year_convert_func(str_input):
    # 문자열 년도 슬라이싱
    str_input = str_input[:2] # 실질적으로 str_input에 들어있는 데이터는 2자리(년도 앞자리) !

    # 문자열이 숫자로만 구성되었는지 확인
    if str_input.isdigit():
        int_input = int(str_input) # 문자열 -> 정수형 형 변환
        
        # 2000년대 처리
        if int_input >= 0 and int_input <= 21:
            result = int_input + 2000 # 2000 더하기
            return result
        
        # 1900년대 처리
        else:
            result = int_input + 1900 # 1900 더하기
            return result
    
    # 문자열이 숫자로만 구성되어있지 않을때
    else:
        print("생년의 일자가 숫자가 아닙니다.")
        return 0

# 월 변환 함수
def month_convert_func(str_input):
    # 문자열 월 슬라이싱
    str_input = str_input[2:4] # 실질적으로 str_input에 들어있는 데이터는 2자리(월에 해당하는 문자) !

    # 문자열이 숫자로만 구성되었는지 확인
    if str_input.isdigit():
        int_input = int(str_input) # 문자열 -> 정수형 형 변환
        
        # 월에 해당하는 숫자의 범위가 1~12 사이일 때
        if int_input >= 1 and int_input <= 12:
            return int_input
        
        # 아닐때
        else:
            print("월이 1~12의 범위 내에 포함되지 않습니다.")
            return 0
    
    # 문자열이 숫자로만 구성되어있지 않을때
    else:
        print("생월의 일자가 숫자가 아닙니다.")
        return 0

# 일 변환 함수
def day_convert_func(str_input, int_year, int_month):
    # 문자열 일 슬라이싱
    str_input = str_input[4:6]

    # 문자열이 숫자로만 구성되었는지 확인
    if str_input.isdigit():
        int_input = int(str_input) # 문자열 -> 정수형 형 변환

        # 1, 3, 5, 7, 8, 10, 12월 처리
        if int_month == 1 or int_month == 3 or int_month == 5 or int_month == 7 or int_month == 8 or int_month == 10 or int_month == 12:
            # 일자가 1~31일 일 때
            if int_input >= 1 and int_input <= 31:
                return int_input
            
            # 아닐때
            else:
                print("일이 해당 월 범위에 포함되지 않습니다.")
                return 0
        
        # 2월 처리
        elif int_month == 2:
            # 윤년일 때
            if leap_year_convert_func(int_year) == True:
                # 일자가 29일 일 때
                if int_input >= 1 and int_input <= 29:
                    return int_input
                
                # 아닐때
                else:
                    print("일이 해당 월 범위에 포함되지 않습니다.")
                    return 0
            
            # 윤년이 아닐때
            else:
                # 일자가 28일 일 때
                if int_input >= 1 and int_input <= 28:
                    return int_input
                
                # 아닐때
                else:
                    print("일이 해당 월 범위에 포함되지 않습니다.")
                    return 0

        # 4, 6, 9, 11월 처리
        elif int_month == 4 or int_month == 6 or int_month == 9 or int_month == 11:
            # 일자가 30일 일 때
            if int_input >= 1 and int_input <= 30:
                return int_input
            
            # 아닐때
            else:
                print("일이 해당 월 범위에 포함되지 않습니다.")
                return 0
        
        # int_month에 0(False)이 들어왔을때
        else:
            print("일이 해당 월 범위에 포함되지 않습니다.")
            return 0
            
    
    # 문자열이 숫자로만 구성되어있지 않을때
    else:
        print("생일의 일자가 숫자가 아닙니다.")
        return 0

# 주민 정보 변환 함수
def resident_convert_func(str_input, int_year):
    # 문자열 주민 정보 슬라이싱
    str_input = str_input[7:] # str_input에 저장되어 있는 숫자는 - 뒷자리 모두(맨 앞은 인덱스 [0]번으로 시작 !) !

    # 문자열이 숫자로만 구성되었는지 확인
    if str_input.isdigit():
        # 1900년 ~ 1999년 사이 판단
        if int_year >= 1900 and int_year <= 1999:
            # 주민번호 앞 자리가 1 혹은 2일 때
            if str_input[0] == "1" or str_input[0] == "2":
                return int(str_input)
            
            # 아닐때
            else:
                print("1900년 ~ 1999년 출생자는 번호가 1 또는 2로 시작합니다.")
                return 0
        
        # 2000년 이상 판단
        else:
            # 주민번호 앞 자리가 3 혹은 4일 때
            if str_input[0] == "3" or str_input[0] == "4":
                return int(str_input)
            
            # 아닐때
            else:
                print("2000년 이후 출생자는 번호가 3 또는 4로 시작합니다.")
                return 0
    
    # 문자열이 숫자로만 구성되어있지 않을때
    else:
        print("주민등록번호 뒷자리가 숫자가 아닙니다.")
        return 0

# isVaild 함수
def isVaild(str_input):
    # 주민등록번호의 글자 수 확인
    if len(str_input) == 14:
        # "-"의 갯수 및 위치 판단 파트

        int_count = 0 # "-"의 갯수를 세기 위한 변수 count

        for i in str_input:
            if i == "-":
                int_count += 1
        
        # "-"가 1개일 때
        if int_count == 1:
            # "-"가 index 6번 자리에 있을때
            if str_input[6] == "-":
                # 함수 이용
                int_year = year_convert_func(str_input) # 년도 변환 함수를 이용해 int_year에 저장
                int_month = month_convert_func(str_input) # 월 변환 함수를 이용해 int_month에 저장
                int_day = day_convert_func(str_input, int_year, int_month) # 일자 변환 함수를 이용해 int_day에 저장
                int_resident_data = resident_convert_func(str_input, int_year) # 주민 정보 변환 함수를 이용해 int_resident_data에 저장

                # 해당 값들이 0이 아닐때
                if int_day != 0 and int_resident_data != 0:
                    return True
                
                else:
                    return False
            
            else:
                print("주민등록번호에 '-'가 적절한 위치에 있지 않거나 없습니다.")
                return False
        
        # 아닐때
        else:
            print("주민등록번호에 '-'가 적절한 위치에 있지 않거나 없습니다.")
            return False
    
    else:
        print("주민등록 번호의 길이가 맞지 않습니다.")
        return False

# 프로그램 작동 파트
str_input = input("주민등록번호를 입력해주세요: ")

if isVaild(str_input) == True:
    print("주민등록번호가 적합해 보입니다.")

else:
    print("주민등록번호가 적합하지 않습니다.")
