#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 11:40
# @Author  : Hython.com
# @File    : electric_car.py
# @IDE     : PyCharm

class Car():
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表数据更新
        禁止将里程数回调
        """
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程数增加指定量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        pass

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        """电动车没有这个属性"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
print(my_tesla.fill_gas_tank())