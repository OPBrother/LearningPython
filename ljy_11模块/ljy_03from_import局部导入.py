# from 模块名 import 工具名
from ljy_11模块.ljy_01测试模块1 import say_hello
from ljy_11模块.ljy_02测试模块2 import Cat
from ljy_11模块.ljy_02测试模块2 import say_hello   # 注意，同名会覆盖之前的导入


TOM = Cat("TOM")
say_hello()
