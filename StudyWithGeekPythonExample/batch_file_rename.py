
import os
import argparse

def batch_rename(work_dir,old_ext,new_ext):
    files = os.listdir(work_dir)
    print(files)
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)

        root_name,file_ext = split_file

        if old_ext == file_ext:
            newfile = root_name + new_ext

            os.rename(os.path.join(work_dir,filename),
                      os.path.join(work_dir,newfile)
                      )

        print("rename is done")
        print(os.listdir(work_dir))


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='the directory where to change extension')
    parser.add_argument('old_ext',metavar = 'OLD_EXT',type=str,nargs=1,help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext

    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir,old_ext,new_ext)
    #batch_rename(work_dir, old_ext, new_ext)





if __name__ == '__main__':
    main()