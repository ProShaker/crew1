#데이터베이스 파일을 불러온다. 비슷한 변수명이 많아 task_07_DB임을 명시해준다.
import task_07_DB

#메뉴 선택창을 출력하는 함수
def func_menu() : 
    print("\n")  
    print("1. 도서 추가(도서명, 저자, 출판연도, 출판사명, 장르 입력)\n")
    print("2. 도서 검색 ", "(2-1. 도서명, 저자, 출판연도, 출판사명, 장르 로 개별적 검색가능)\n")
    print("3. 도서 정보 수정\n")
    print("4. 도서 삭제\n")
    print("5. 현재 총 도서 목록 출력 (도서명, 저자, 출판일, 출판사명, 장르 출력)\n")
    print("6. 저장(읽어들인 입력파일에 저장한다.)\n") 
    print("7. 프로그램 나가기(자동저장)\n")


def func_add_book() :  
    s = str(input("도서명, 저자, 출판연도, 출판사명, 장르 순으로 입력해주세요. : "))
    task_07_DB.book_lists.append(s)                                                               
    print("저장하시면 해당 도서가 목록에 포함됩니다.")

#input.txt에 입력
def func_save_book() :
    new_file = open("input.txt", "w")
    for i in task_07_DB.book_lists:
        new_file.write("{} \n".format(i))
    new_file.close()
    print("저장됐습니다.")
    
def func_search_book() : 
    #numb은 검색한 인덱스를 저장할 리스트
    numb = [] 
    category_book = input("\n도서명, 저자, 출판연도, 출판사명, 장르 중에 검색 분야를 입력해주세요. : ")
    print("\n")
    if(category_book == "도서명") :
        title_b = input("도서명 검색 함수 실행..찾고자 하는 도서명을 입력해주세요. : ")

        for i in range(len(task_07_DB.book_title)):
            if(title_b == task_07_DB.book_title[i]) : numb.append(i)

    elif(category_book == "저자") : 
        writer_b = input("저자명 검색 함수 실행..찾고자 하는 저자명을 입력해주세요. : ")

        for i in range(len(task_07_DB.book_writer)):
            if(writer_b == task_07_DB.book_writer[i]) : numb.append(i)
    
    elif(category_book == "출판연도") : 
        year_b = input("출판연도 검색 함수 실행..찾고자 하는 출판연도를 입력해주세요. : ")

        for i in range(len(task_07_DB.book_year)):
            if(year_b == task_07_DB.book_year[i]) : numb.append(i)

    elif(category_book == "출판사명") : 
        publisher_b = input("출판사명 검색 함수 실행..찾고자 하는 출판사명을 입력해주세요. : ")
        
        for i in range(len(task_07_DB.book_publisher)):
            if(publisher_b == task_07_DB.book_publisher[i]) : numb.append(i)
    else : 
        genre_b = input("장르명 검색 함수 실행..찾고자 하는 장르명을 입력해주세요. : ")

        for i in range(len(task_07_DB.book_genre)):
            if(genre_b == task_07_DB.book_genre[i]) : numb.append(i)

    print("도서명, 저자, 출판연도, 출판사명, 장르 순입니다.\n")
    for i in map(int, numb):
        print(task_07_DB.book_lists[i])
    
def func_print_books():
    print("\n도서명, 저자, 출판연도, 출판사명, 장르 순입니다.\n")
    for i in range(len(task_07_DB.book_lists)) :
        print(i+1,"번", task_07_DB.book_lists[i])

def func_rewrite_book() :
    func_print_books()
    numb = int(input("\n수정할 행번호를 입력해주세요. (1부터 시작): "))
    task_07_DB.book_lists[numb - 1] = input("도서명, 저자, 출판연도, 출판사명, 장르 순으로 입력해주세요. : ")

def func_remove_book() : 
    func_print_books()
    numb = int(input("\n제거할 행을 입력해주세요. (1부터 시작): "))
    del task_07_DB.book_lists[numb - 1]

def func_getout() : 
    print("프로그램을 종료합니다. 자동 저장합니다.")
    func_save_book()
    quit()