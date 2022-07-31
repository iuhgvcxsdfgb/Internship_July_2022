'''
Problem :

One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.


refer full question :https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

'''
#Solution


a = int(input());
b = int(input());
print(a//b);
print(a%b);
print(divmod(a,b));
