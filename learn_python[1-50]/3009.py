cx = []
cy = []
x = 0; y = 0
for i in range(3):
    n, m = map(int, input().split())
    cx.append(n)
    cy.append(m)
for i in range(3):
    if cx.count(cx[i]) == 1:
        x = cx[i]
    if cy.count(cy[i]) == 1:
        y = cy[i]
print(x, y)
