# pip install peewee
from models.bookstore import Book, Category
import models.bookstore as bs
# booksore 모듈을 bs 별칭으로 import

# 테이블 생성 테스트: 모델 매핑 정보를 기반으로
def create_table_test():
    bs.initialize()

# insert와 relation 테스트
from datetime import datetime

def insert_relation_test():
    # 카테고리 생성
    c1 = bs.insert_category(no = 1, name = "Python")
    c2 = bs.insert_category(no = 2, name = "Java")

    # Book insert
    bs.insert_book(no = 1, title = "Learning Python", pub_date=datetime(2015, 11, 13), price = 10000, category=c1)
    #c1은 foreighn key 참조
    bs.insert_book(no=2, title="히치하이커 Python", pub_date=datetime(2018, 3, 4), price=18000, category=c1)
    bs.insert_book(no=3, title="Effective Java", pub_date=datetime(2103, 7, 8), price=21000, category=c2)
    bs.insert_book(no=4, title="God of Java", pub_date=datetime(2008, 1, 15), price=15000, category=c2)

# Update
# 별도의 메서드가 있는 것은 아니고 get등으로 메모리에 적제
# 필드변경, save() 메서드로 수행
def update_test():
    # title이 Effective Java인 책을 찾아와서 각격을 변경
    book = Book.get(Book.title == "Effective Java")
    # 업데이트 할 필드를 수정
    book.price += book.price * 0.1
    #print(book) # __str__
    print("업데이트 된 Book객체:", book)
    book.save() #저장->업데이트

# Delete: .get 메서드로 메모리에 적재한 이후
# delete_instance()메서드로 메모리에서 지우면
# 테이블로부터도 삭제
def delete_test():
    book = Book.get(title = "God of Java")
    # 메모리로부터 삭제 -> delete
    book.delete_instance()

# select
def select_test():
    books = Book.select() # 모든 컬럼 모든 레코드를 추출
    print(books.sql()) # 실제 수행된 SQL 문을 확인 할 수 있다

    for book in books:
        print(book)

# select 컬럼의 제한: projection
def projection_test():
    # 레코드 추출시 특정 컬러만 추출할 경우
    # 필요한 필드의 목록을 select()메서드 내에 선언
    books = Book.select(Book.title, Book.price)

    for book in books:
        print("책제목 {}: {}원".format(book.title, book.price))

# where와  order by
def where_order_test():
    # 가격이 15000원 이상,  20000원 미만인 모든 책의 목록
    # 가격의 역순으로 추출
    books = Book.select().where((Book.price >= 15000) &
                                (Book.price < 20000)).order_by(Book.price.desc())
    print("SQL:", books.sql())

    for book in books:
        print("검색된 책:", book)


# ForeighnKeyField 타입으로 작성된 컬럼 타입에
# related_name이 설정되어 있다면 역참조가 가능하다
# PK-FK를 기반으로
def reverse_reference_test():
    # 카테고리 내에 포함된 모든 책을 참조
    categories = Category.select()
    for category in  categories:
        print("카테고리:", category)
        # related_name에 설정한 이름으로 역참조 가능
        print("카테고리 내의 책들:")
        for book in category.books:
            print(book)

if __name__ == "__main__":
    #create_table_test()
    #insert_relation_test()
    #update_test()
    #delete_test()
    #select_test()
    #projection_test()
    #where_order_test()
    reverse_reference_test()