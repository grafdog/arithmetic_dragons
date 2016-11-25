# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
class Hero(Attacker):
    _health = 100
    _attack = 1000000
    _experience = 0
    name = 'a'
    def __init__(self,name):
        self.name = name

    def attack(self, target):
        super().attack(target)
        self._experience += 1
