#coding=utf-8

import threading
import time




def test1(temp):
    temp.append(33)
    print("---in test1---%s" % str(temp))

def test2(temp):
    print("---in test2---%s" % str(temp))

num_list = [11,22]


def main():
    t1 = threading.Thread(target=test1,args=(num_list,))
    t2 = threading.Thread(target=test2,args=(num_list,))
    t1.start()

    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main thread --%s " % str(num_list))





if __name__ == "__main__":
    main()