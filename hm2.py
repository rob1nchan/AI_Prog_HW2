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


# 定义ExamSystem逻辑控制类，封装所有系统功能
class ExamSystem:
    def __init__(self, file_path: str):
        # 初始化系统：文件路径、学生字典（学号为键，Student对象为值）
        self.file_path = file_path
        self.students: Dict[str, Student] = {}
        # 程序启动时自动初始化读取学生信息
        self.init_students()

    def init_students(self):
        """初始化学生信息：读取文本文件并封装为Student对象"""
        try:
            # 以只读模式打开文件，处理FileNotFoundError异常
            with open(self.file_path, 'r', encoding='utf-8') as f:
                # 读取所有行并跳过表头行（第一行）
                lines = f.readlines()[1:]
                for line in lines:
                    # 去除行首尾空白并按制表符分割（匹配txt文件的制表符分隔格式）
                    line = line.strip()
                    if not line:  # 跳过空行，避免数据解析错误
                        continue
                    parts = line.split('\t')
                    # 按列解析：序号(0)、姓名(1)、性别(2)、班级(3)、学号(4)、学院(5)
                    _, name, gender, cls, id_num, college = parts
                    # 将班级转为整数，封装为Student对象并加入字典
                    self.students[id_num] = Student(id_num, name, gender, int(cls), college)
            print("✅ 学生信息初始化成功！")
        except FileNotFoundError:
            # 处理文件丢失异常，友好提示并退出程序
            print(f"❌ 错误：未找到文件 {self.file_path}，请检查文件路径是否正确！")
            exit(1)
        except Exception as e:
            # 处理其他数据解析异常，捕获并提示具体错误
            print(f"❌ 学生信息解析失败：{str(e)}")
            exit(1)

    def find_student_by_id(self, id_num: str):
        """根据学号查找学生信息"""
        if id_num in self.students:
            # 学号存在，打印学生信息（调用__str__方法）
            print(self.students[id_num])
        else:
            # 学号不存在，友好错误提示
            print(f"❌ 未查询到学号为【{id_num}】的学生信息！")

    @staticmethod
    def check_number_input(input_str: str, max_num: int) -> int:
        """
        静态方法：校验用户输入的数字是否合法（满足OOP静态方法要求）
        :param input_str: 用户输入的字符串
        :param max_num: 输入数字的最大值（总学生数）
        :return: 合法的整数
        """
        try:
            # 转换为整数，处理非数字输入的ValueError
            num = int(input_str)
            if 1 <= num <= max_num:
                return num
            else:
                # 处理数字超出范围的情况
                raise ValueError(f"输入数字必须在1-{max_num}之间")
        except ValueError as e:
            # 抛出统一异常，由调用方捕获
            raise ValueError(f"❌ 输入非法：{str(e)}")

    def random_call(self):
        """随机点名功能：输入数量，返回不重复随机学生"""
        total = len(self.students)
        if total == 0:
            print("❌ 暂无学生信息，无法点名！")
            return
        # 获取用户输入并校验
        input_num = input(f"请输入点名人数（1-{total}）：")
        try:
            call_num = self.check_number_input(input_num, total)
            # 随机选择指定数量的不重复学号（random.sample实现无重复抽样）
            random_ids = random.sample(list(self.students.keys()), call_num)
            # 打印点名结果
            print(f"\n🎯 随机点名{call_num}人结果：")
            for idx, id_num in enumerate(random_ids, 1):
                print(f"{idx}. {self.students[id_num]}")
        except ValueError as e:
            # 捕获校验方法的异常，友好提示
            print(e)