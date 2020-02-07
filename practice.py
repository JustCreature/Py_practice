"""This is the list of my practical work of learning OOP. (Uncomment he part of code you want to run)"""


"""Class and object creation"""

#
# import random
#
# class Warrior:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#
#     def gotHurt(self):
#         self.hp -= 20
#
#
# first = Warrior('first')
# second = Warrior('second')
#
# while first.hp > 0 and second.hp > 0:
#     turn = random.randint(0, 1)
#     if turn == 0:
#         whoAt = first
#         whoHurt = second
#     else:
#         whoAt = second
#         whoHurt = first
#     whoHurt.gotHurt()
#     txt = f"The {whoAt.name} attaced the {whoHurt.name}\n" \
#         f"The {whoHurt.name} has {whoHurt.hp} lives"
#     print(txt)
#
# print("The first won") if first.hp > 0 else print("The second won")

###################
###################

"""Constructor __init__"""

# import random

# class Employee:
#     def __init__(self, name, last_name, quall=1):
#         self.name = name
#         self.last_name = last_name
#         self.quall = quall
#
#     def info(self):
#         return self.name + self.last_name + self.quall
#
#     def __del__(self):
#         return print(f"Goodbye Mr.{self.name} {self.last_name}")
#
#
# person1 = Employee('Ivan', 'Ivanov', random.randint(1, 5))
# person2 = Employee('Nikolay', 'Nikolayev')
# person3 = Employee('Sergey', 'Sergeyev', random.randint(1, 5))
#
# emps = []
# emps.append(person1)
# emps.append(person2)
# emps.append(person3)
#
# arr = []
# arr.append(person1.quall)
# arr.append(person2.quall)
# arr.append(person3.quall)
# weak = arr.index(min(arr))
#
# emps[weak].__del__()
#
# input()

#################
#################

"""Inheritance"""

# import random
#
#
# class Person:
#     def __init__(self, id, team):
#         self.id = id
#         self.team = team
#
#
# class Hero(Person):
#     def __init__(self, id, team):
#         Person.__init__(self, id, team)
#         self.level = 0
#
#     def level_up(self):
#         self.level += 1
#
# class Soldier(Person):
#     def follow_hero(self, my_hero):
#         pass
#
#
# hero1 = Hero(1, 1)
# hero2 = Hero(2, 2)
#
# sold1 = []
# sold2 = []
#
# i = 0
#
# while i < random.randint(10, 15):
#     check = random.randint(1, 2)
#     if check == 1:
#         sold = Soldier(i, 1)
#         sold1.append(sold)
#     else:
#         sold = Soldier(i, 2)
#         sold2.append(sold)
#
#     i += 1
#
# hero1.level_up() if len(sold1) > len(sold2) else hero2.level_up()
#
# x = sold1[random.randint(0, len(sold1))]
# x.follow_hero(hero1)
#
# print(f"Hero 1 level is {hero1.level}")
# print(f"Hero 2 level is {hero2.level}")
#
# print(f"Soldier {x.id} is following hero {hero1.id}")


############################
############################

"""Polimorphism"""

#
# class Thing:
#     def __init__(self, material):
#         self.material = material
#
#     def __add__(self, other):
#         if self.material == other.material:
#             return f"The room furniture is made of {self.material}"
#         else:
#             return "The room furniture is made of different materials"
#
#
# class Table(Thing):
#     def somethig(self):
#         pass
#
#
# class Chair(Thing):
#     def anything(self):
#         pass
#
#
# table = Table(str(input("Enter material of table...\n")))
# chair = Chair(str(input("Enter material of chair...\n")))
#
# print(table + chair)
#

###############################
###############################

"""Encapsulation"""

#
# class Calculate:
#     __usage = 0
#
#     def __init__(self, a, b):
#         self.val = Calculate.__calk(a, b)
#
#     def __setattr__(self, attr, value):
#         if attr == 'val':
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError
#
#     def __calk(a, b):
#         return a * b / 2 * b
#
#     def get_val(self):
#         return self.val
#
#     def set_usage(n):
#         Calculate.__usage = n
#
#     def get_usage():
#         return Calculate.__usage
#
# q = Calculate(5, 5)
# print(q.get_val())
#
# q.val = 5
# print(q.get_val())
#
# i = 0
#
# while i != '':
#     i += 1
#     q = input("First number\n")
#     if q == 'exit':
#         print(f"Goodbye. You used the function {Calculate.get_usage()} times")
#         break
#     w = input("Second number\n")
#     if w == 'exit':
#         print(f"Goodbye. You used the function {Calculate.get_usage()} times")
#         break
#     q = int(q)
#     w = int(w)
#     print(Calculate(q, w).get_val())
#     Calculate.set_usage(i)
#


###################################
###################################

"""Composition"""

# import math
# import sys
#
# class Room:
#     def __init__(self, width, length, height):
#         self.set_sides(width, length, height)
#         self.wd = []
#
#     def getRolls(self, l, w):
#         self.__rolls = math.ceil(self.get_work_surface() / (l * w))
#
#     def set_sides(self, width, length, height):
#         self.__width = width
#         self.__length = length
#         self.__height = height
#
#     def lastDel(self):
#         self.wd.pop()
#
#     def clearWD(self):
#         self.wd.clear()
#
#     def addWD(self, w = 1, h = 1):
#         self.wd.append(WinDoor(w, h))
#
#     def get_work_surface(self):
#         self.__work_surf = self.get_square()
#         if len(self.wd) > 0:
#             for i in self.wd:
#                 self.__work_surf -= i.get_sq()
#         return self.__work_surf
#
#     def get_square(self):
#         self.__square = 2 * self.__height * (self.__length + self.__width)
#         return self.__square
#
#
# class WinDoor:
#     def __init__(self, x, y):
#         self.__square = x * y
#
#     def get_sq(self):
#         return self.__square
#
#
# ask = 0
#
# while ask != 'exit':
#     try:
#         l = float(input("Enter your room width\n"))
#         w = float(input("Enter your room length\n"))
#         h = float(input("Enter your room height\n"))
#         r1 = Room(l, w, h)
#     except ValueError:
#         print("Incorrect input")
#         break
#
#     while ask != exit:
#         ask = input("\nWhat do you want? Choose ONE!!!\n1 - Count square, 2 - Count the amount of rolls, "
#                   "3 - Add window-door,\n4 - delete last added window-door, 5 - Count work surface, "
#                   "6 - New room parametrs,\nexit - stop the program\n")
#         if not str(ask).isdigit() and ask != 'exit' or ask == ' ' or ask == '':
#             print("Incorrect input")
#             sys.exit()
#         if ask == 'exit':
#             sys.exit()
#         ask = int(ask)
#         if ask == 1:
#             print(f"\nThe square is {r1.get_square()}\n")
#         elif ask == 2:
#             l = float(input("The length of your roll:\n"))
#             w = float(input("The width of your roll:\n"))
#             print(f"\nYou'll need {r1.getRolls(l, w)} rolls\n")
#         elif ask == 3:
#             try:
#                 l = float(input("The length of your window-door(or leave it empty):\n"))
#                 w = float(input("The width of your window-door(or leave it empty):\n"))
#                 r1.addWD(l, w)
#             except ValueError:
#                 pass
#             r1.addWD()
#         elif ask == 4:
#             r1.lastDel()
#         elif ask == 5:
#             print(f"\nThe work surface is {r1.get_work_surface()}\n")
#         elif ask == 6:
#             break
#     print("GoodBye")

##########################
##########################

"""Operator overload"""

#
# class Snow:
#     def __init__(self, q):
#         self.q = q
#
#     def __add__(self, other):
#         return self.q - other.q
#
#     def __sub__(self, other):
#         return self.q + other.q
#
#     def __mul__(self, other):
#         return self.q / other.q
#
#     def __truediv__(self, other):
#         return self.q // other.q
#
#     def __call__(self, ar):
#         self.q = ar
#
#     def makeSnow(self, row_quant):
#         self.qw = self.q / row_quant
#         i = 0
#         row = ''
#         while i < self.qw:
#             row += row_quant * "*" + "\n"
#             i += 1
#         return row
#
#
# s1 = Snow(20)
# s2 = Snow(50)
# x = s1 + s2
# print(x)
# print(s1.makeSnow(5))
# s1(10)
# print(s1.makeSnow(5))
#


#####################################
#####################################

"""Modules and packages"""

#
# import geometry
# from geometry import planimetry as pl, stereometry as st
#
# b = st.Ball(5)
# a = pl.Circle(5)
#
# print(a.length(), b.V())
#
# print(geometry.stereometry.__doc__)
#

########################
########################

"""Just prog"""

#
# import random
#
#
# class Data:
#     def __init__(self, *info):
#         self.info = info
#
#     def __getitem__(self, item):
#         return self.info[item]
#
#
# class Teacher:
#     def teach(self, info, *pupil):
#         for i in pupil:
#             i.take(info)
#
#
# class Pupil:
#     def __init__(self):
#         self.knowledge = []
#
#     def take(self, info):
#         self.knowledge.append(info)
#         self.knowledge = set(self.knowledge)
#         self.knowledge = list(self.knowledge)
#
#     def forget(self):
#         self.out = random.randint(0, len(self.knowledge) - 1)
#         self.knowledge.pop(self.out)
#
#
# lesson = Data('class', 'object', 'inheritance', 'polimorphism', 'encapsulation')
# marIvanna = Teacher()
# vasya = Pupil()
# petya = Pupil()
#
# marIvanna.teach(lesson[2], vasya, petya)
# marIvanna.teach(lesson[0], petya)
#
# print(f"Vasya knows {vasya.knowledge}")
# print(f"Petya knows {petya.knowledge}")
#
# i = 0
# for i in range(3):
#     selfEd = random.randint(0, len(lesson.info) - 1)
#     petya.take(lesson[selfEd])
#     vasya.take(lesson[selfEd])
#
# petya.forget()
#
# print(f"Vasya knows {vasya.knowledge}")
# print(f"Petya knows {petya.knowledge}")
#

#####################
#####################

"""Static methods"""

#
# from math import pi
#
# class Cylinder:
#     @staticmethod
#     def __make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return round(circle*2 + side, 2)
#
#     def __init__(self, diametr, hight):
#         self.diametr = diametr
#         self.hight = hight
#         self.__count_area()
#
#     def __count_area(self):
#         self.__area = self.__make_area(self.diametr, self.hight)
#
#     def __setattr__(self, key, value):
#         if key != 'diametr' or key != 'hight':
#             self.__dict__[key] = value
#         else:
#             raise AttributeError
#
#     def get_area(self):
#         self.__count_area()
#         return self.__area
#
#
# a = Cylinder(1, 2)
# print(a.get_area())
#
# print(a._Cylinder__make_area(2, 2))
#
# a.diametr = 2
#
# print(a.get_area())
#

########################
########################












