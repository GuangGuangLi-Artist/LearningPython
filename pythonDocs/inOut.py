# -*- coding:utf-8 -*-

"""输入和输出 
1.格式化字符串字面值
2.格式化字符串字面值中的等号表达式 
3.使用字符串的 format() 方法
4.格式化数字
5.文件读写
6.文件和目录路径
"""


class InOut:
    def __init__(self):
        pass

    def format_string_literals(self):
        """格式化字符串字面值
        Python 3.6 引入了一种新的字符串格式化方法，称为格式化字符串字面值（f-strings）。
        这种方法允许在字符串中直接嵌入表达式，并在运行时进行求值。
        """
        name = "Alice"
        age = 30
        greeting = f"Hello, my name is {name} and I am {age} years old."
        print(greeting)  # 输出: Hello, my name is Alice and I am 30 years old.

    def format_string_literals_with_eq(self):
        """格式化字符串字面值中的等号表达式
        Python 3.8 引入了在 f-strings 中使用等号表达式的功能。
        这种功能允许你在字符串中直接显示变量名和其对应的值，方便调试和日志记录。
        """
        x = 42
        y = "hello"
        debug_info = f"{x=}, {y=}"
        print(debug_info)  # 输出: x=42, y='hello'

    def using_format_method(self):
        """使用字符串的 format() 方法
        在 Python 中，字符串的 format() 方法提供了一种灵活的方式来格式化字符串。
        这种方法允许你通过位置参数或关键字参数来插入变量值。
        """
        name = "Bob"
        age = 25
        greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
        print(greeting)  # 输出: Hello, my name is Bob and I am 25 years old.

    def formatting_numbers(self):
        """格式化数字
        Python 提供了多种方式来格式化数字，包括使用 f-strings 和 format() 方法。
        你可以指定数字的精度、填充字符、对齐方式等。
        """
        number = 1234.56789
        formatted_number_fstring = f"{number:.2f}"  # 保留两位小数
        formatted_number_format = "{:.2f}".format(number)  # 保留两位小数
        print(formatted_number_fstring)  # 输出: 1234.57
        print(formatted_number_format)  # 输出: 1234.57
        large_number = 1234567890
        formatted_large_number = f"{large_number:,}"  # 使用逗号作为千位分隔符
        print(formatted_large_number)  # 输出: 1,234,567,890
    
    

    def formatting_range(self):
        for i in range(1, 11):
            print('{0:2d} {1:3d} {2:4d}'.format(i, i*i, i*i*i))

    def formatting_dictStr(self):
        table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
        for name, phone in table.items():
            #在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
            print(f'{name:10} ==> {phone:10d}')



    
    def file_read_write(self):
        """文件读写
        Python 提供了内置的 open() 函数来处理文件的读写操作。
        你可以使用不同的模式（如 'r' 读取，'w' 写入，'a' 追加）来打开文件。
        """
        # 写入文件
        with open("example.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")

        # 读取文件
        with open("example.txt", "r") as file:
            content = file.read()
            print(content)
        # 输出:
        # Hello, World!
        # This is a test file.
    def file_and_directory_paths(self):
        """文件和目录路径
        Python 的 os 和 pathlib 模块提供了处理文件和目录路径的强大工具。
        你可以使用这些模块来创建、删除、重命名文件和目录，以及
        获取文件的属性等。
        """
        import os
        from pathlib import Path

        # 使用 os 模块
        current_directory = os.getcwd()
        print(f"Current Directory: {current_directory}")

        new_directory = os.path.join(current_directory, "new_folder")
        os.makedirs(new_directory, exist_ok=True)
        print(f"Created Directory: {new_directory}")

        # 使用 pathlib 模块
        path = Path(current_directory) / "new_folder"
        print(f"Path exists: {path.exists()}")

        # 列出目录内容
        for item in path.iterdir():
            print(item.name) # 输出目录中的文件和子目录名称


if __name__ == "__main__":
    io = InOut()
    io.format_string_literals()
    io.format_string_literals_with_eq()
    io.using_format_method()
    io.formatting_numbers()
    io.formatting_range()
    io.formatting_dictStr()
    io.file_read_write()
    io.file_and_directory_paths()