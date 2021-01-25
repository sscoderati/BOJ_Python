arr = []
for i in range(1, 9):
    arr.append(i)
arr_ds = sorted(arr, reverse = True)
arr_input = list(map(int, input().split()))
if arr_input == arr:
    print("ascending")
elif arr_input == arr_ds:
    print("descending")
else:
    print("mixed")
