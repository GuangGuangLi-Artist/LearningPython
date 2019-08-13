# coding=utf-8


def print_info(name, title="", gender=True):
    """
    :param title:
    :param name:
    :param gender:
    :return:
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" % (title,name, gender_text))


# 缺省参数，需要使用 **最常见的值** 作为默认值
# 必须保证** **带有默认值的缺省参数** **在参数列表末尾**
print_info("李广")
print_info("老王")
print_info("小妹", gender=False)
