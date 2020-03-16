#퀴즈
def ex_1_1():
    str = "Life is too short, You need Python".lower().replace(",", "").replace(" ", "")
    print(str, type(str))
    lst = list(str)
    chars = set(lst)
    print(chars)
    lst = list(chars)
    print(sorted(lst), "LENGTH:" , len(sorted(lst)))



def ex_1_2():
    """
    리스트의 인덱스, 슬라이스, 치환에 관한 퀴즈입니다.
파일명은 quiz01_2.py로 저장합니다
다음과 같이 리스트가 선언되어 있습니다.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
리스트 내부의 순서를 일부 뒤집어 다음과 같은 결과를 만들고자 합니다.
[1, 2, 3, 7, 6, 5, 4, 8, 9, 10]
Instruction:

리스트로부터 [4, 5, 6, 7]을 추출하여 slice 에 담아 봅시다.
slice의 순서를 뒤집어 봅시다.
lst의 적절한 부분에 slice를 끼워 넣어 봅시다.
    :return:
    """
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Slice:", lst[3:7])
    slice = lst[3:7]
    slice.reverse()
    print("Reverse Slice:", slice)
    lst[3:7] = slice
    print(lst)

def ex_1_3():
    """
    리스트와 사전을 다루는 퀴즈입니다.
파일명은 quiz01_3.py로 저장합니다
다음과 같이 사전을 포함한 리스트가 선언되어 있습니다.
students = [
    {
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]
두 학생의 kor, eng, math 합계 점수와 평균을 사전 데이터에 "total", "average" 키값으로 넣어 봅시다.
    :return:
    """
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]

    print(type(students))
    """
    print({**students[0], **students[1]}, {**students[1], **students[1]})
    total_kim = students[0]["kor"] + students[0]["eng"] + students[0]["math"]
    print(total_kim)
    avg_kim = total_kim / 3
    print(avg_kim)
    total_lee = students[1]["kor"] + students[1]["eng"] + students[1]["math"]
    print(total_lee)
    avg_lee = total_lee / 3
    print(avg_lee)
    keys = ("total", "avg")
    values = (total_kim, avg_kim)
    kim = dict(zip(keys, values))
    print("kim의 총점과 평균:", kim)
    keys = ("total", "avg")
    values = (total_lee, avg_lee)
    lee = dict(zip(keys, values))
    print("lee의 총점과 평균:", lee)
    students[0]["total"] = total_kim
    students[0]["avg"] = avg_kim
    students[1]["total"] = total_lee
    students[1]["avg"] = avg_lee
    print(students)
    """
    for student in students:
        print()










if __name__=="__main__":
    #ex_1_1()
    #ex_1_2()
    ex_1_3()