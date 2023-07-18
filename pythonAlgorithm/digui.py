#递归

"""
基线条件：指函数何时不再调用自己
递归条件：函数调用自己
"""

#写一个倒计时程序

def countTime(i):
    print(i)
    if i<=0:
        return
    else:
        countTime(i-1)



if __name__ == "__main__":
    countTime(3)