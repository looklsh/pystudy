# dict 예제
def define_dict():
    """사전의 정의"""

    #기본적인 사전의 생성
    dct = dict() #빈사전
    print(dct, type(dct))
    #Literal 이용한 생성 {}
    dct = {"basketball": 5, "baseball": 9}
    #키에 접근하고자 할 경우
    print(dct["baseball"]) # baseball 키에 연결된 값을 참조
    #없는 키에 연결된 값의 참조
    # print(dct["soccer"]) # -> KeyError
    dct["soccer"] = 11 #새 값을 넣을 경우 새로운 키
    print("dct:", dct)

    #순서가 없기 때문에 인덱싱, 슬라이싱 불가
    #len, 포함 여부 확인 가능
    # -> 기본적으로 대상이 key를 기준으로 한다(값이 아니다)

    #길이의 확인: len
    print(dct, "LENGTH:", len(dct))

    #in, not in 키를 검색할 수 있다
    print("soccer" in dct) # 키 목록에서 soccer를 검색
    print("volleyball" in dct)

    # dict는 복합 자료형 -> 키의목록, 값의 목록을 별도로 뽑아낼 수있다
    print("KEYS of dct:", dct.keys()) #keys 메서드 -> 키목록
    print("Types of keys:", type(dct.keys()))
    print("Values of dct:", dct.values()) # values 메서드 -> 값목록

    #값의 포함 여부를 판단하여면 .values() dict_values를 추출
    # 그 안에서 확인
    #dct의 값에 9가 포함되어 있는가?
    print("9 in dct.values()?", 9 in dct.values())

    #사전을 생성하는 다른 방법들
    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1="value1", key2="value2", key3="value3")
    print("d1:", d1, type(d1))

    #튜플의 리스트로 사전의 생성
    d2 = ([("key1", 1), ("key2", 2), ("key3", 3)])
    print("d2:", d2, type(d2))

    # 키의 목록과 값의 목록이 이미 있는 경우
    #zip 객체로 묶어서 dict에 전달
    keys = ("one", "two", "three", "four")
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print("d3:", d3, type(d3))

    #사전의 키는 immutable 자료형이어야 함
    d4 ={}
    d4[True] = "True"
    d4[10] = 10
    d4["eleven"] = 11
    d4[("홍길동", 23)] = "홍길동 23"
    # bool, 수치형, 문자열, 튜플 등 불변 자료형 가능
    # d4 [["홍길동", 23]] = "홍길동 23" # -> 에러
    print("d4:", d4)

def dict_method():
    """사전의 메서드들"""
    dct = {"soccer": 11, "baseball": 9, "volleyball": 6}
    print("dct:", dct)
    #key의 목록 추출: keys 메서드
    keys = dct.keys()
    print("keys of dct:", keys, type(keys))
    #dict_keys는 순차 자료형으로 변환 할 수 있다
    keys_list = list(keys)
    print(keys_list)
    # 값의 목록  추출: values 메서드
    values = dct.values()
    print("Values of dct:", values, type(values))
    #키-값 쌍 튜플의 목록 추출
    pairs = dct.items()
    print("keys-Value of dct:", pairs)

    dct.clear() # 비우기
    print("dct:", dct)

def using_dict():
    """사전 사용 연습"""
    phones = {"홍길동": "010-1234-5678",
              "장길산": "010-9876-5432",
              "임꺽정": "010-5678-9012"}
    print(phones)

    #새로운 키의 추가['키']
    phones['일지매'] = "010-3333-3333"
    print(phones)

    #키 직접 점근 vs get 비교
    if "고길동" in phones:
        print(phones['고길동']) # 키 직접 접근은 키가 없으면 에러 발생
    print(phones.get('고길동')) # get 메서드는 키가 없을 경우 NONE 리턴
    # 키가 없어도 기본값을 리턴하고자 할 경우 get 메서드 두번째 인자로 기본값을 부여
    print(phones.get("고길동", "미등록"))

    # 삭제: del
    if "일지매" in phones:
        del phones['일지매']
    print(phones)

    #pop 메서드: 값을 가져오며 해당 객체를 삭제
    print(phones.pop('장길산'))
    print(phones)
    # popitem 메서드: 키-밸류 쌍튜플을 반환하고 키를 삭제
    item = phones.popitem()
    print("Name:", item[0], "phone:", item[1])
    print(phones)

def loop():
    """사전 객체의 순회"""
    phones = {"홍길동": "010-1234-5678",
              "장길산": "010-9876-5432",
              "임꺽정": "010-5678-9012"}
    print(phones)

    # 기본적인 loop
    for key in phones: # 루프를 진행하면 keys() 목록을 대상으로 한다
        print(key, ":", phones[key])

    # 키와 값을 함께 loop
    for key, value in phones.items(): # item 메서드는 키-값 쌍튜플의 목록
        print(key, ":", value)



if __name__=="__main__":
    #define_dict()
    #dict_method()
    #using_dict()
    loop()