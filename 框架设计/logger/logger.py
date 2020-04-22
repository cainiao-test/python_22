import logging

# logger 日志收集器
logger_22 = logging.getLogger('python22的日志收集器')

# 设置日志收集器的级别
logger_22.setLevel(logging.DEBUG)

# 控制台显示 日志处理器
concole_handler = logging.StreamHandler()

# 初始化文件处理器
file_handler = logging.FileHandler('demo.log', encoding='utf-8')

# 日志收集器添加处理器
logger_22.addHandler(concole_handler)
logger_22.addHandler(file_handler)

concole_handler.setLevel(logging.DEBUG)

# 设置输出格式
console_fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s")
concole_handler.setFormatter(console_fmt)

file_fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s")
file_handler.setFormatter(file_fmt)

logger_22.warning('22期')

# 1 收集器
# 2 设置收集器级别
# 3 初始化处理器
# 4 处理器的级别
# 5 添加处理器
# 6 初始化格式器
# 7 设置处理器的格式


def run(a, b):
    try:
        a/b
    except:
        logger_22.error('报错啦')

run(2, 0)