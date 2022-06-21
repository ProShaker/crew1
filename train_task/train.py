import datetime

file_path = "C:/Users/dktk5/Documents/GitHub/crew1/train_task/TrainList(1).txt"

train_list = []
ticket_number = 0
list_len = 0

#빠른시간 기차 검색 및 예매 함수
def search_ticket() :

    search_train = []
    global list_len
    global train_list
    global ticket_number

    #개행문자로 구분지어 텍스트 파일을 불러온다.
    with open(file_path) as f:
        temp_list = f.read().splitlines()

    #공백을 기준으로 배열의 원소를 나누어 train_list에 재할당
    for i in range(len(temp_list)) :
        train_list.append(temp_list[i].split())

    
    list_len = len(temp_list)

    print('빠른시간 기차 검색 및 예매화면입니다.\n')
    print('원하는시간, 출발역, 도착역, 열차종류를 입력해주세요.\n')
    _time = input('원하는 시간 (hh:mm): ')
    _departure = input('출발역 (00역): ')
    _arrival = input('도착역 (00역): ')
    _type = input('열차종류 (KTX/새마을호): ')

    #텍스트 파일에서 첫 번째 문자열을 제외하고 반복문을 실행한다.
    for i in range(1, list_len):
        
        #입력받은 정보와 train_list를 비교하여 가장 빠른 기차를 찾는다.
        if (_departure == train_list[i][1]) and (_arrival == train_list[i][3]) and (_type == train_list[i][4]) and (train_list[i][5] != '매진'):
            if datetime.datetime(2000, 11, 22, int(_time[0:2]), int(_time[3:5])) < datetime.datetime(2000, 11, 22, int(train_list[i][0][0:2]), int(train_list[i][0][3:5]) ) :
                
                #찾은 정보를 정리한다.
                search_train = ' '.join(map(str, train_list[i]))

                #예매한 열차의 인덱스를 전역변수에 저장
                ticket_number = i
                break;
    
    #반복문 실행 후에도 리스트가 비어있다면 다음 문장 출력  
    if not search_train  : 
        print("작성 형식에 문제가 있거나 해당 기차의 좌석은 전부 매진됐습니다.\n")
        

    #리스트에 특정 기차 정보가 들어가있다면 다음 문장 실행
    else : 
        print(search_train, '\n')
        _answer = input('해당 기차로 예매하시겠습니까? (y/n) : ')
        print('\n')

        #예매했을 경우 남은 좌석수 -1
        if(_answer == 'y') : 
            print("예매되었습니다.\n")
            train_list[i][5] = int(train_list[i][5]) - 1

            #좌석수가 0이 될 경우 매진으로 표시
            if train_list[i][5] == 0 : 
                train_list[i][5] = '매진'

            #위에서 작성한 내용을 바탕으로 파일을 다시 작성한다.
            with open(file_path, 'w') as file_data:
                for i in range(list_len) :
                    train_list[i].append('\n')
                    train_list[i] = ' '.join(map(str, train_list[i]))
                    file_data.write(train_list[i])
            
        # y 제외한 키를 누를 시 
        else : 
            print("메인화면으로 돌아갑니다.\n")
           

#전체 기차리스트 출력
def print_ticket() :

    global train_list

    for i in train_list :
        print(i)
    input("메뉴화면으로 돌아가시려면 아무 키나 눌러주세요.\n")

#예매현황 출력 및 취소
def manage_ticket():

    global ticket_number
    global train_list

    #0으로 초기화한 값이 그대로 남아있을 시 티켓 x
    if ticket_number == 0:
        print("티켓이 조회되지 않습니다.\n")

    #티켓의 인덱스가 정해져있다면 다음 문장 실행
    else:
        print("나의 예매 현황\n")
        print(train_list[ticket_number])
        _answer = input("\n 1. 예매 취소\n 2. 뒤로 가기\n\n 메뉴선택 : ")
        print('\n')

        #예매취소 선택시
        if _answer == '1' :
            print("예매가 취소되었습니다.\n\n")

            #좌석 연산을 위해 배열로 변환
            temp_list = train_list[ticket_number].split()
            #좌석이 숫자가 아니라 "매진" 문자열일 확률 고려
            if temp_list[5] == '매진' : temp_list[5] = 1
            else : temp_list[5] = int(temp_list[5]) + 1
            #배열을 문자열로 변환
            train_list[ticket_number] = ' '.join(map(str,temp_list))

            with open(file_path, 'w') as file_data:
                for i in range(list_len) :
                    file_data.write(train_list[i])
                    

        else :
            input("메뉴화면으로 돌아가시려면 아무 키나 눌러주세요.\n")
while 1: 
        
    print('원하는 열차 정보와 시간를 입력하면 가장 가까운 시간대에 열차를 출력하며, 예매를 진행하는 프로그램\n')
    print(' 1. 빠른시간 기차 검색 및 예매 \n')
    print(' 2. 전체 기차 리스트 출력 \n')
    print(' 3. 나의 예매 현황 출력 및 예매 취소 \n')
    print(' 4. 프로그램 종료 \n')
    num = int(input('원하시는 메뉴 번호를 선택해주세요. : '))
    print('\n')

    if num == 1:
        search_ticket()

    elif num == 2:
        print_ticket()

    elif num == 3:
         manage_ticket()

    elif num == 4:
         print('프로그램을 종료합니다.\n')
         exit()
    else:
        print('없는 번호를 누르시면 안됩니다.\n\n')



        
