#coding=utf-8

import cards_tools

while True:
    # TODO(李广) 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作: ")
    print("您选择的操作是[%s]" % action_str)

    if action_str in ["1", "2", "3"]:
        #新增名片
        if action_str == "1":
            cards_tools.new_cards()

        #显示全部
        elif action_str == "2":
            cards_tools.show_all()

        #查询名片
        elif action_str == "3":
            cards_tools.search_cards()
    elif action_str == "0":
        print("欢迎再次使用名片管理系统")
        break
    else:
        print("您输入的内容有误，请重新输入")
