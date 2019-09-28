#coding=utf-8


try:
    num = int(input("请输入一个整数:"))

    result = 8 / num

    print(result)

except ValueError:
    print("请输入一个整数")
#捕获未知错误
except Exception as result:
    print("未知错误 %s" %result)

else:
    print("尝试成功")

finally:
    print("不管是否成功都会去执行")

print("*" * 50)