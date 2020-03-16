# 예외 처리
"""
try:
    코드
except: 익셉션 타입 as 익셉션 할당 변수:
    처리
else:
    정상 수행 되었을 때의 처리
finally:
    예외유무 관계없이 항상 마지막에 실행
    주로 자원 정리작업에 활용
    """

def handilng_exception():
    """예외 처리 연습"""
    # 인덱스 에러
    # 캐스팅 에러 value Error
    # 사전 키 접근 에러
    # 정수를 0으로 나웠을 경우 zerodivisionerror

    lst = []

    try:
        #lst[3] = 1 # 인덱스 에러
        4 / 1 # zerodivisionerror
        #int("Stirng") # valueError
    except ValueError as e:
        print("정수로 변환할 수 없습니다.", e)
    except ZeroDivisionError as e:
        print("정수를 0으로 나눌 수 없습니다", e)
    except IndexError as e:
        print("인덱스 범위가 벗어났습니다", e)
    except Exception as e:
        # Exception은 모든 예외의 부모 클래스
        print("Exception:", e)
    else:
        print("예외 없이 코드가 실행되었습니다")
    finally:
        print("예외 여부 관계 없이 항상 마지막에 실행")

def raise_exception():
    def beware_dog(animal):
        if animal.lower() == "dog":
            # 강제 익셉션 발생
            raise RuntimeError("강아지는 출입을 제한 합니다")
        else:
            print("어서오세요!")

    try:
        beware_dog("cow")
        beware_dog("cat")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))



if __name__=="__main__":
    #handilng_exception()
    raise_exception()
