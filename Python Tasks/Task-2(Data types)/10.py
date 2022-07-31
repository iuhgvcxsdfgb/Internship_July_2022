'''
Task
You have a non-empty set , and you have to execute N commands given in N  lines.

The commands will be pop, remove and discard.

refer full question :https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

'''
#Solution

n = int(input())
s = set(map(int, input().split()))
num = int(input())
for i in range(num):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))
