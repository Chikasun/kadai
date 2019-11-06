# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6


data = input('データを入力してください(スペース区切り) > ')
data_list = []
for s in data.split(' '):
    data_list.append(int(s))

print(f'合計値: {sum(data_list)}')
print(f'最大値: {max(data_list)}')
print(f'最小値: {min(data_list)}')
print(f'平均値: {sum(data_list) // len(data_list)}')
