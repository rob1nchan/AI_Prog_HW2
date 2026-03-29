# 导入Python标准库，满足作业库使用限制
import os
import random
import time
from typing import List, Dict

# 定义Student数据类，满足OOP硬性要求
class Student:
    def __init__(self, id_num: str, name: str, gender: str, cls: int, college: str):
        # 初始化学生属性：学号、姓名、性别、班级、学院
        self.id_num = id_num    # 学号
        self.name = name        # 姓名
        self.gender = gender    # 性别
        self.cls = cls          # 班级
        self.college = college  # 学院

    def __str__(self):
        # 重写__str__魔术方法，实现学生信息的友好打印
        return f"姓名：{self.name}，性别：{self.gender}，班级：{self.cls}班，学号：{self.id_num}，学院：{self.college}"

