'''
Topic : Tuple
Given an integer, , and  space-separated integers as input, create a tuple, t , of those n integers.
Then compute and print the result of hast(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t));
