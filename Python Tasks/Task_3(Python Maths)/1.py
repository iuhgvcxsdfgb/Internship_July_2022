'''
Task
ABC is a right triangle, 90o at B.
Therefore, angle ABC = 90o.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC in degrees.

refer full question :https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

'''


#solution

import math
ab=int(input())
bc=int(input())
ca=math.hypot(ab,bc)
mc=ca/2
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')
