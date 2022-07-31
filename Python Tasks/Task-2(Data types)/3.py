'''
Topic : Nested Lists
The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
refer full question : https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''

# Solution

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);    
