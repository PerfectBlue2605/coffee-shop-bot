import DataBase

class Counter:
    def __set_name__(self, owner, name):
        self.name = '__'+name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        setattr(instance,self.name,value)

class Items:
    count = Counter()
    type = Counter()
    def __init__(self, count, type = 'None'):
        self.count = count
        self.type = type
    #Milk
milk_farm = Items(1,'Farm')
milk_luga = Items(0,'Luga')
milk_koks = Items(0,'Coconut')
milk_slivki = Items(0,'Cream')
milk_nemol = Items(0,'Nemoloko')
milk_prosto = Items(0,'Prostokvashino')
milk_sib = Items(0,'Sibmol')

#Coffee
coffee = Items(0)
cocoa = Items(0)
hot_chocolate = Items(0)

#Stuff
check_line = Items(10)
cup_450 = Items(100)
cup_350 = Items(100)
cup_250 = Items(100)
cup_cap_big = Items(100)
cup_cap_small = Items(100)
sugar = Items(100)

#change_value
def change_value(item, value):
    item.count = value
#add value
def add_value_1(item):
    item.count += 1
def add_value_5(item):
    item.count += 5
def add_value_10(item):
    item.count += 10
def add_value_12(item):
    item.count += 12
#reduce value
def reduce_value_1(item):
    item.count -= 1
def reduce_value_5(item):
    item.count -= 5
def reduce_value_10(item):
    item.count -= 10
def reduce_value_12(item):
    item.count -= 12
#DataBase defs:
def unpack(hstable):
    return
# def main():
#
# if __name__ == '__main__':
#     main()