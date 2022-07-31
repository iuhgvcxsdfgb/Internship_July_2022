'''
Topic : Introduction to set
refer full question : https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
'''

#Solution


N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))
