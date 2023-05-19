"""
module로 사용되는 figure.py는 
class인 line을 이용하여 선의 길이를 설정/참조하며
area_square -> 정사각형의 넓이
area_circle -> 원의 넓이
area_regular_triangle -> 삼각형의 넓이
를 반환합니다.
"""

import math

class line :
    """
    line class는 선의 길이에 대해 저장하고 있는 클래스이며,
    __length를 통해 변수를 외부에서 접근하는 것을 금지시켰습니다.
    또한 해당 변수를 수정, 접근을 위해 
    함수 set_length과 get_length를 사용하고 있습니다.
    """
    __length = 0
    
    def __init__(self, length) :
        """
            생성자의 초기 length 값을 받습니다.
        """
        self.__length = length

    def set_length(self, length) :
        """
        length의 길이를 수정합니다.
        """
        self.__length = length
    
    def get_length(self) :
        """
        length의 길이를 반환합니다.
        """
        return self.__length

def area_square(length) : # 정사각형의 넓이 반환
    return length * length

def area_circle(length) : # 원의 넓이 반환
    return length * length * math.pi

def area_regular_triangle(length) : # 삼각형의 넓이 반환
    return math.sqrt(3) / 4 * (length * length)
