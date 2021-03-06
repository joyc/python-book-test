#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/03 22:59
# @Author  : Hython.com
# @File    : car.py
# @IDE     : PyCharm
"""该类用于表示汽车和电动汽车的基本属性的类"""
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

class Battery():
    """一次模拟电车电瓶的尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的容量信息"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动车的特有属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()


# my_new_car = Car('audi', 'A4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)