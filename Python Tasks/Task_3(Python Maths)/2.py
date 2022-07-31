'''
Task
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

refer full question :https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true

'''
#solution


for i in range(1, int(input())+1):
    print(((10**i)//9)**2)
