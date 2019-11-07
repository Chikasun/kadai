class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + ' ' + self.family_name

    def age(self):
        return self.age

    def entry_fee(self):
        if self.age <= 3:  # C-5
            return 0
        if self.age < 20:
            return 1000
        if self.age >= 20 and self.age < 65:
            return 1500
        if self.age >= 65:
            return 1200
        if self.age >= 75:  # C-6
            return 500

    def info_csv(self):
        return self.full_name(), str(self.age), str(self.entry_fee())


ken = Customer('Ken', 'Tanaka', 15)
tom = Customer('Tom', 'Ford', 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

# C-1
# "Ken Tanaka" という値を返す
print(ken.full_name())
# "Tom Ford" という値を返す
print(tom.full_name())

# C-2
# ken.age  # 15 という値を返す
print(ken.age)
# tom.age # 57 という値を返す
print(tom.age)
# ieyasu.age # 73 という値を返す
print(ieyasu.age)

# C-3
# ken.entry_fee()  # 1000 という値を返す
print(ken.entry_fee())
# tom.entry_fee() # 1500 という値を返す
print(tom.entry_fee())
# ieyasu.entry_fee() # 1200 という値を返す
print(ieyasu.entry_fee())

# C-4
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
print(','.join(ken.info_csv()))
# ken.info_csv()  # "Tom Ford,57,1500" という値を返す
print(','.join(tom.info_csv()))
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
print(','.join(ieyasu.info_csv()))

# C-7
print('\t'.join(ken.info_csv()))

# C-8
print('|'.join(ken.info_csv()))
