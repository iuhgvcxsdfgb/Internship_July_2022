'''
The first line consists of an integer,K , the size of each group.
The second line contains the unordered elements of the room number list.

refer full question :https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

'''


#Solution

N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if(i != len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break;
    else:
        print(storage[i])
