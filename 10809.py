s = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
            'v','w','x','y','z']
for i in alphabet:
    if s.count(i) >= 1:
        print(s.index(i), end = ' ')
    else:
        print(-1, end = ' ')
