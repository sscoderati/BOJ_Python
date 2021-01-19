score = []
sum = 0
for i in range(0, 5):
    tmp = int(input())
    score.append(tmp)
    if score[i] < 40:
        sum += 40
    else:
        sum += score[i]
print(int(sum / len(score)))
