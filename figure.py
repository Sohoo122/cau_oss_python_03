"""
figure 모듈은
line class를 이용하여 선의 길이를 설정/참조하고
area_square, area_circle, area_regular_triangle 함수를 이용하여
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다.
"""

import math

class line :
    """
    class인 line은 선의 길이에 대해 저장하고 있으며, 
    변수로는 외부에서 접근할 수 없는 __width와 __height가 있습니다.
    변수 수정/접근을 위해 set_length와 get_length가 존재합니다.
    """
    __width = 0
    __height = 0
    
    def __init__(self, width, height) : # 초기 width와 height 값을 받습니다.
        self.__width = width # 초기 선의 가로 길이
        self.__height = height # 초기 선의 세로 길이

    def set_length(self, width, height) : # 선의 길이를 수정합니다.
        self.__width = width # 수정하고자 하는 가로 길이
        self.__height = height # 수정하고자 하는 세로 길이
    
    def get_length(self) : # 선의 길이를 반환합니다.
        return self.__width, self.__height

def area_rectangle(width, height) : # 직사각형의 넓이를 반환합니다.
    if width <= 0 or height <= 0 : raise ValueError
    return width * height

def area_ellipse(width, height) : # 원의 넓이를 반환합니다.
    if width <= 0 or height <= 0 : raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height) : # 정삼각형의 넓이를 반환합니다.
    if width <= 0 or height <= 0 : raise ValueError
    return width * height / 2