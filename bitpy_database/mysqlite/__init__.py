# __init__.py
# 해당 디렉터리를 패키지로 인식하게 하는 파일
# 패키지 import시  초기화를 담당하는 역할
from .database import *
__all__ = ['Database'] # 필요한 객체만 공개하고자 할 경우
# import *