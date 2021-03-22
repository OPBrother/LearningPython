'''
import logging


# 一：日志配置
logging.basicConfig(
    # 1.日志输出位置：1、终端 2、文件
    # filename = 'access.log', # 不指定，默认打印到终端

    # 2.日志格式
    format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(messgage)s',

    # 3、时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',

    # 4、日志级别
    # critical => 50
    # error => 40
    # warning => 30
    # info => 20
    # debug => 10
    level=30
)

# 二：输出日志
logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重错误critical')
'''

import ljy_11模块.ljy_日志配置字典

# !!!强调!!!
# 1、logging是一个包，需要使用其下的config、getLogger，可以如下导入
# from logging import config
# from logging import getLogger

# 2、也可以使用如下导入
import logging.config       # 这样连同logging.getLogger都一起导入了,然后使用前缀logging.config.

# 3、加载配置
logging.config.dictConfig(ljy_11模块.ljy_日志配置字典.LOGGING_DIC)

# 4、输出日志
logger1=logging.getLogger('用户交易')
logger1.info('egon儿子alex转账3亿冥币')

# logger2=logging.getLogger('专门的采集') # 名字传入的必须是'专门的采集'，与LOGGING_DIC中的配置唯一对应
# logger2.debug('专门采集的日志')



