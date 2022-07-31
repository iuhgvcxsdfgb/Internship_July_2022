'''
Problem :

You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.
If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

refer full question :https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

'''
#Solution

T = int(input())

for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))
