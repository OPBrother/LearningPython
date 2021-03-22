import os
import shutil


# 识别zip
def scan_file():
    files = os.listdir()
    for f in files:
        if f.endswith('.zip'):
            return f


def unzip_it(f):
    # 解压zip
    folder_name = f.split('.')[0]
    target_path = "./" + folder_name
    shutil.unpack_archive(f, target_path)


# 删除zip
def delete(f):
    os.remove(f)


while True:
    zip_file = scan_file()
    # 判断zip_file是否为空
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)