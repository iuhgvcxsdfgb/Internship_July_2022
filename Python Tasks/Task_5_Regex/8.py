'''
Input Format

The first line contains a single integer, n, denoting the number of email address.
Each line  I of the N  subsequent lines contains a name and an email address as two space-separated values following this format:

name <user@email.com>

Output Format

Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:

name <user@email.com>

'''
#Solution

import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)
