#coding=utf-8

import copy


nums = [11,22]

list_reverse_before = ['a','b','c','d']

def test_nums(temp):
    temp.append(33)


def main():

    #test_nums(nums)   [11, 22, 33]


    #[11, 22]
    test_nums(copy.deepcopy(nums))





    print(nums)

    #反转字符列表
    list_reverse_after = list_reverse_before[::-1]
    print(list_reverse_after)





if __name__ == "__main__":
    main()
