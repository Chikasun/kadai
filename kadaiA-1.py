# A-1
# 　リスト[]
users = ['Bob', 'Tom', 'Ken']

# A-2
int_numbers = [1, 2, 3, 4, 5]

# A-3
kazuma_info = ['Kazuma', 'Takahashi', 35]

# A-4
members = ['Kazuma', 'Makoto', 'Ohira']

# A-5
print(kazuma_info)

# A-6
# for リストの値 in 変数名
odd_numbers = [1, 3, 5, 7, 9]
for odd_number in odd_numbers:
    print(odd_number)

# A-7
even_numbers = [2, 4, 6, 8]
for even_number in even_numbers:
    print(even_number * 2)

# A-8
# 辞書{キー：値}
# for キー　in 辞書名名
# print(キー名（キー）,辞書名[キー名]（値）)'
users_info = {'Kazuma': 35, 'Tom': 57, 'Bob': 77}
for user_info in users_info:
    print(f'Name:{user_info},Age:{users_info[user_info]}')

# A-9
kazuma_info = {'first_name': 'Kazuma', 'family_name': 'Takahashi', 'age': 35}
print(kazuma_info["first_name"])
print(kazuma_info["family_name"])
print(kazuma_info["age"])

# A-10
import random


def dice():
    print(random.randint(1, 6))


# # A-11
# Height(m)? > 170
# Weight(kg)? > 60
# Your BMI is 20.76

Height = int(input('How　tall are you?')) / 100
Weight = int(input('What is your weight?'))

BMI = Weight / (Height ** 2)
print(f'Your BMI is {BMI:.2f}')
