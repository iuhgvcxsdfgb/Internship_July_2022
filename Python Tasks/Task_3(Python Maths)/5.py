'''
Problem :

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2^31 - 1 (c++ int) or 2^63 - 1 (C++ long long int).
As we know, the result of a^b grows really fast with increasing b.
Let's do some calculations on very large integers.

refer full qution : https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true

'''
#solution


A = int(input())
B = int(input())
C = int(input())
D = int(input())

print((A**B)+(C**D))
