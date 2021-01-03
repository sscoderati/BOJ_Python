s = input()
cnt = s.count(' ')
if(s.startswith(' ') == True and s.endswith(' ') == True):
    cnt -= 2
elif(s.startswith(' ') != s.endswith(' ')):
    cnt -= 1
else:
    pass
print(cnt + 1)
