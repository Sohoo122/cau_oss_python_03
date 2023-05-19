"""
figure 모듈은
line class를 이용하여 선의 길이를 설정/참조하고
area_square, area_circle, area_regular_triangle 함수를 이용하여
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다.
"""

import math

class line :
    """
    class은 line은 선의 길이에 대해 저장하고 있으며, 
    변수로는 외부에서 접근할 수 없는 __length가 있습니다.
    변수 수정/접근을 위해 set_length와 get_length가 존재합니다.
    """
    __length = 0
    
    def __init__(self, length) : # 초기 length 값을 받습니다.
        self.__length = length

    def set_length(self, length) : # 선의 길이를 수정합니다.
        self.__length = length
    
    def get_length(self) : # 선의 길이를 반환합니다.
        return self.__length

def area_square(length) : # 정사각형의 넓이를 반환합니다.
    return length * length

def area_circle(length) : # 원의 넓이를 반환합니다.
    return length * length * math.pi

def area_regular_triangle(length) : # 정삼각형의 넓이를 반환합니다.
    return math.sqrt(3) / 4 * (length * length)