#Script Name :  creat_dir_if_not_there.py
#Author      :  Li
#Created     :  25th Angust 2020
#Version     :   1.0.0


import os
def main():
    Message = 'The directory already exsits'
    TESTDIR = 'Postman'
    try:
        home = os.path.expanduser("~")
        print(home)

        if not os.path.exists(os.path.join(home,TESTDIR)):
            os.makedirs(os.path.join(home,TESTDIR))
        else:
            print(Message)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()