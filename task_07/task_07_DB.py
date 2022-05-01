#데이터베이스 파일
file_path = "input.txt"                                    

#원본 파일에 있는 값을 리스트로 받아온다.
with open('input.txt', 'rt') as f:        
    book_lists = f.readlines()

#개행문자를 지운다.
book_lists = [line.rstrip('\n') for line in book_lists]              

book_title = []
book_writer = []
book_year = []
book_publisher = []
book_genre = []

#반복문을 통해 제목, 작가 등에 대한 데이터 베이스를 만든다.
for i in range(len(book_lists)):                              
    temp = list(book_lists[i].split())
    book_title.append(temp[0])
    book_writer.append(temp[1])
    book_year.append(temp[2])
    book_publisher.append(temp[3])
    book_genre.append(temp[4])