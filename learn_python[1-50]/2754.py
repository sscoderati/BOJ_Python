import sys

grade = input()
score = 0
if grade[0] == 'A':
    score = 4.0
elif grade[0] == 'B':
    score = 3.0
elif grade[0] == 'C':
    score = 2.0
elif grade[0] == 'D':
    score = 1.0
else:
    print(0.0)
    sys.exit()
if grade[1] == '+':
    score += 0.3
elif grade[1] == '-':
    score -= 0.3
else:
    pass
print(score)
