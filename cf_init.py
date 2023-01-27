'''
复制该文件夹下的A.py到以下文件（如果文件存在，直接替换；如果不存在，创建该文件）：
A2.py
B.py
B2.py
C.py
C2.py
D.py
D2.py
E.py
E2.py
F.py
F2.py
G.py
G2.py
H.py
H2.py
I.py
I2.py

对于A.rs文件，执行同样的操作，覆盖A2.rs,B.rs……I2.rs
对于A.cpp文件，执行同样的操作，覆盖A2.cpp,B.cpp……I2.cpp
对于A.c文件，执行同样的操作，覆盖A2.c,B.c……I2.c
'''
import os
import shutil
import sys

def copy_file(src, dst):
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy(src, dst)

def copy_files(suf):
    src = 'A.' + suf
    for i in range(9):
        ch = chr(ord('A') + i)
        dst = ch + '.' + suf
        if src != dst:
            copy_file(src, dst)
            print('copy {} to {}'.format(src, dst))
        dst = ch + '2.' + suf
        copy_file(src, dst)
        print('copy {} to {}'.format(src, dst))
        copy_file('ATC_'+src, 'ATC_'+dst)
        print('copy ATC_{} to ATC_{}'.format(src, dst))

def main():
    copy_files('py')
    copy_files('cpp')
    copy_files('c')
    print('Done')

if __name__ == '__main__':
    main()