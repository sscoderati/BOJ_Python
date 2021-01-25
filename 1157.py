word = input().lower()
alpha_word = list(set(word))
cnt = []

for i in alpha_word:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(alpha_word[cnt.index(max(cnt))].upper())
