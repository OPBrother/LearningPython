from distutils.core import setup

'''
制作模块压缩包步骤：
在Project 里new一个setup.py文件
在doc命令中在project上运行 python setup.py build
再运行 python setup.py sdict
'''
setup(name="ljy_message",                       # 包名
      version="1.0",                            # 版本
      description="ljy的发送和接收消息模块",        # 描述信息
      long_description="完整的发生和接受消息模块",   # 完整描述信息
      author="林均煜",                           # 作者
      author_email="2276720277@qq.com",         # 作者邮箱
      url="www.xxxxxx.com",                     # 主页
      py_modules=["ljy_message.send_message",   #
                  "ljy_message.receive_message"])

