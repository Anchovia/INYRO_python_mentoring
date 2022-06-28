import sys # sys.stdin.readline()을 이용하기 위해 라이브러리 import

# main 함수
def main():
    dataList = [0] * 10000 # 1부터 10000까지의 숫자를 담기 위한 배열 선언

    n = int(sys.stdin.readline().rstrip()) # 입력 받을 데이터의 양을 받음

    # 데이터 입력받음
    for i in range(0, n):
        data = int(sys.stdin.readline())

        # 데이터에 해당하는 인덱스에 대하여 그 인덱스의 값 + 1
        dataList[data - 1] += 1

    # 1만까지의 인덱스 모두 출력(0인 경우 패스, 0이 아닌 경우 그 숫자 번 만큼 해당 인덱스 + 1의 숫자 출력)
    for k in range(0, len(dataList)):
        if(dataList[k] != 0):
            for i in range(0, dataList[k]):
                print(k + 1)
        
        else:
            pass

# __main__
main()
