# %%

# 길이를 입력받고 정사각형, 원, 삼각형의 넓이를 반환해주는 파이썬 파일
import figure

myline = figure.line(10)

square = figure.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)