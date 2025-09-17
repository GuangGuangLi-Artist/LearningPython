# -*- coding: utf-8 -*-

"""异常和错误处理
1.捕获异常  
2.抛出异常
3.自定义异常
4.使用 finally 块
5.使用上下文管理器处理资源
6.调试和日志记录
"""

import logging

class ExceptDemo:

    def __init__(self):
        pass
    def capture_exceptions(self):
        """捕获异常
        在 Python 中，异常处理是通过 try-except 块来实现的。 你可以捕获特定类型的异常，并对其进行处理。
        """ 
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print(f"Caught an exception: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print(f"Result is {result}")
        finally:
            print("Execution completed.")
    
    def raise_exceptions(self):
        """抛出异常
        在 Python 中，你可以使用 raise 语句来抛出异常。 这对于自定义错误处理非常有用。
        """
        def divide(a, b):
            if b == 0:
                raise ValueError("The denominator cannot be zero.")
            return a / b
        try:
            result = divide(10, 0)
        except ValueError as e:
            print(f"Caught an exception: {e}")  
        else:
            print(f"Result is {result}")
        
    
    def custom_exceptions(self):
        """自定义异常
        你可以通过继承内置的 Exception 类来创建自定义异常类。
        """
        class CustomError(Exception):
            pass
        def risky_function():
            raise CustomError("This is a custom error message.")
        try:
            risky_function()
        except CustomError as e:
            print(f"Caught a custom exception: {e}")
    
    def using_finally_block(self):
        """使用 finally 块
        finally 块中的代码无论是否发生异常都会执行，通常用于清理资源。
        """
        try:
            file = open("example1.txt", "r")
            content = file.read()
            print(content)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        finally:
            if 'file' in locals():
                file.close()
                print("File closed.")
    
    def using_context_manager(self):
        """使用上下文管理器处理资源
        使用 with 语句可以简化资源管理，如文件操作，确保资源在使用后正确释放。
        """
        try:
            with open("example1.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
    
    def debugging_and_logging(self):
        """调试和日志记录
        Python 提供了 logging 模块，用于记录程序运行时的信息，帮助调试和监控。
        """
       
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug("This is a debug message.")
        logging.info("This is an info message.")
        logging.warning("This is a warning message.")
        logging.error("This is an error message.")
        logging.critical("This is a critical message.")
    
if __name__ == "__main__":
    demo = ExceptDemo()
    demo.capture_exceptions()
    demo.raise_exceptions()
    demo.custom_exceptions()
    demo.using_finally_block()
    demo.using_context_manager()
    demo.debugging_and_logging()