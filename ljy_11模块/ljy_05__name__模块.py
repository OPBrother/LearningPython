# 模块会导入全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具


def say_hello():
    print("你好你好，我是...")

def main():
    # 如果在当前文件执行，__name__永远是__main__ (是字符串)
    # 如果是当作模块被执行，__name__是__模块名__
    print(__name__)

    print("小明开发的模块")
    say_hello()


# 所以要想主函数代码不被外界执行
if __name__ == "__main__":
    main()
