import os


def func(path, ceng):
    lst = os.listdir(path)

    for name in lst:
        real_path = os.path.join(path, name)
        if os.path.isdir(real_path):     # 判断是否为文件
            print("|--" * ceng + name)
            func(real_path, ceng+1)
        else:
            print("|--" * ceng + name)


if __name__ == '__main__':
    func("F:\jp_workspace", 0)

