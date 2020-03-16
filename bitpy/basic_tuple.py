#Tuple연습
def define_tuple():
    """
    튜플의 정의
    """
    """
    튜플
    -리스트와 거의 비슷하나 immutable
    -(), tuple 객체함수 이용
    -요소 값이 1개일 경우 , 찍어줘야 한다
    """
    tp = tuple()
    print(tp, type(tp))

    tp2 = () # 공튜플(literal)
    tp3 = (1,) # 항목이 1개면 뒤에 ,찍어줘야함
    tp4 = (1, 2, 3)
    print(tp2, tp3, tp4)

def tuple_oper():
    """튜플의 연산자"""
    # len, 포함여부
    # 인덱스 접근, 슬라이싱 가능
    # immutable 자료형 -> 내부 자료 변경 불가
    # 반복과 연결
    tp = 1, 2, 3, 4, 5 # ()안써줘도 튜플로 인식
    print(tp, "LENGTH:", len(tp))
    #포함여부 확인
    print("3 in tp?", 3 in tp)
    #인덱스 접근
    print("정인덱스 tp:", tp[0], tp[1], tp[2])
    print("역인덱스 tp:", tp[-5], tp[-4], tp[-3])
    # 슬라이싱[시작경계:끝경계:간격]
    print("슬라이싱 tp:", tp[1:4], type(tp[1:4]))
    print("튜플 전체:", tp[:]) # 튜플 전체
    #반복(*int)
    print("반복 tp:", tp * 2)
    #연결(+ 튜플)
    print("연결 tp:", tp + (6, 7, 8))

def tuple_assignment():
    """튜플의 할당"""
    #튜플을 활용, 여러 개의 변수를 동시 할당
    x, y, z = 10, 20, 30
    print(x, y, z)

    #튜플을 ㅣ용한 변수의 값 swap(값 교체)
    x, y = 10, 20
    print("x={}, y={}".format(x, y))
    x, y = y, x
    print("SWAP: x={}, y={}".format(x, y))

def tuple_method():
    """튜플의 메서드들"""
    tp = (20, 30, 10, 20)
    #특정 객체의 index
    print(tp.index(20)) # 20 객체의 인덱스
    print(tp.index(20, 1)) # 인덱스 검색의 범위 제한

def packing_unpacking():
    """튜플의 패킹과 언패킹"""
    tp = 10, 20, 30, "Python" # ()없어도 자동으로 패킹
    print(tp, type(tp))
    # 요소의 개수 확인
    print("COUNT:", tp.count(20))  # 내부의 20 객체의 개수

    #기본 언패킹: 튜플의 요소개수만큼 변수를 부여
    a, b, c, d = tp
    print(a, b, c, d)

    # 기본 언패킹은 변수의 개수와 요소의 개수가 동일해야 한다
    # a, b, c = tp #요소의 개수보다 변수가 더 적은 경우 -> 에러
    # a, b, c, d, e = tp # 요소의 개수보다 변수가 더 많은 경우 -> 에러

    #확장 Unpacking
    #지정 되지 않은 개수의 튜플을 할당 받을 변수의 이름 앞에 *
    a, *b = tp
    print("a:", a, type(a))
    print("b:", b, type(b))
    # 앞에서 1개, 뒤에서 1개를 추출
    a, *b, c = tp
    print("a:", a, type(a))
    print("b:", b, type(b))
    print("c:", c, type(c))

def loop():
    """튜플의 순회"""
    tp = (10, 20, 30, 40, 50)
    for item in tp:
        print(item, end=" ")
    print()




if __name__=="__main__":
    #define_tuple()
    #tuple_oper()
    #tuple_assignment()
    tuple_method()
    #packing_unpacking()
    #loop()