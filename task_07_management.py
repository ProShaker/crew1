"""
E-oN task
1. 도서 추가(도서명, 저자, 출판연도, 출판사명, 장르 입력)
2. 도서 검색
(2-1. 도서명, 저자, 출판연도, 출판사명, 장르 로 개별적 검색가능)
3. 도서 정보 수정
4. 도서 삭제
5. 현재 총 도서 목록 출력( 도서명, 저자, 출판일, 출판사명, 장르 출력)
6. 저장(읽어들인 입력파일에 저장한다.)
7. 프로그램 나가기(자동저장)

* 주의사항
- 초기 도서목록으로 input.txt 파일 이외의 다른 파일을 사용하거나 만들지 않는다.
- input파일의 내용을 불러와서 사용하고, 그 input파일에 수정한 내용을 다시 저장하는 방식으로 작성한다.
- 객체지향 언어로 코딩할 것(사람, 도서DB, 도서관리 system 등의 객체로 이루어져야 함). C언어의 경우 객체지향이 아
닌 절차지향으로 작성.
- 객체를 추가해도 되나 사람, 도서DB, 도서관리 system 등의 객체는 별도의 파일로 만들어 서로 import할 것
"""
from task_07_func_define import func_add_book
from task_07_func_define import func_search_book
from task_07_func_define import func_rewrite_book
from task_07_func_define import func_remove_book
from task_07_func_define import func_print_books
from task_07_func_define import func_save_book
from task_07_func_define import func_getout
from task_07_func_define import func_menu
import task_07_DB
def task_07_main():
    while(1):
        func_menu()
        print("데이터 베이스 길이 : ", len(task_07_DB.book_lists))
        print("장르 길이 : ", len(task_07_DB.book_genre))

        numb = int(input("원하는 번호를 선택해주세요. : "))
        if(numb == 1) : 
            func_add_book()
        if(numb == 2) : 
            func_search_book()
        if(numb == 3) : 
            func_rewrite_book()
        if(numb == 4) : 
            func_remove_book()
        if(numb == 5) : 
            func_print_books()
        if(numb == 6) : 
            func_save_book()
        if(numb == 7) : 
            func_getout()
    

