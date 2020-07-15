#coding=utf-8


#把一个字符串变成Unicode码位的列表

#for循环遍历
def run():
    symbols = "$%^&*"
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    return codes


#列表生成式
symbols_out = "$%^&*"
codes_out = [ord(symbol_out) for symbol_out in symbols_out]
print(codes_out)
print("*" * 20)

if __name__ == '__main__':
    codes = run()
    print(codes)