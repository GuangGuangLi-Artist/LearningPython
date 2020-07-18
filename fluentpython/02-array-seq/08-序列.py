#coding=utf-8

#对序列使用+和*
#+ 和 * 都是不修改原有的操作对象，构建一个全新的序列
l = [1,2,3]
m = [4,5,6]
print(l + m)
print(l*5)
#建立由列表组成的列表
board = [["-"] * 3 for i in range(3)]
print(board)
board_1 = [["-"] * 3]
print(board_1)
board[1][2] = 'X'
print(board)