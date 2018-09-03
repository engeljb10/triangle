# content of test_sample.py
import unittest
import math

def classify_triangle(a, b, c):
	right = ""
	if((a+b < c) or (a+c < b) or (c+b < a)):
		return "not a triangle"
	if ((a*a + b*b == round(c*c)) or (a*a + c*c == round(b*b)) or (c*c + b*b == (a*a))):
		right = "right "
	if(a == b and b == c):
		return right + "equilateral"
	if((a == b) or (b==c) or (a == c)):
		return right + "isosceles"
		print(c)
	if (a!=b and b!=c and a!=c):
		return right + "scalene"


if __name__ == '__main__':
	print(classify_triangle(1,2,3))
	print(classify_triangle(2,2,2.8284))
	print(classify_triangle(3,1,1))
	print(classify_triangle(5,4,3))



   