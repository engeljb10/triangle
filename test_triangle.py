import triangle
import math

def test_classify_triangle_scalene():
	result = triangle.classify_triangle(1,2,3)
	assert result == "scalene"
	
def test_classify_triangle_isosceles():
	result = triangle.classify_triangle(2,2,3)
	assert result == "isosceles"

def test_classify_triangle_equilateral():
	result = triangle.classify_triangle(1,1,1)
	assert result == "equilateral"

def test_classify_triangle_right_scalene():
	result = triangle.classify_triangle(3,4,5)
	assert result == "right scalene"

def test_classify_triangle_right_isosceles():
	result = triangle.classify_triangle(1,1,math.sqrt(2))
	assert result == "right isosceles"

def test_classify_triangle_not_a_triangle():
	result = triangle.classify_triangle(1,2,8)
	assert result == "not a triangle"
