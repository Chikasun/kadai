# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24


row = int(input('行数を入力してください:'))
column = int(input('列数を入力してください:'))

for number in range(1, row + 1):
    for column_num in range(1, column + 1):
        print(number * column_num, end=' ')
    print()
