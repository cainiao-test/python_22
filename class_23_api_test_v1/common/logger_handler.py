import logging


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)s-%(message)s"

                 ):
        """初始化函数, 完成level,format,handler 配置"""
        super().__init__(name, level=level)

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)

        # handler的级别
        handler.setLevel(handler_level)

        # 添加handler
        self.addHandler(handler)

        # 设置format
        handler_format = logging.Formatter(fmt)
        handler.setStream(handler_format)


logger = LoggerHandler('python22')
