#coding=utf-8
import logging
class Logger:
    def __init__(self):
        self.logger = logging.getLogger('simple_example')#创建记录器并命名
        self.logger.setLevel(logging.DEBUG)##指定记录器将处理的最低严重性日志消息
        fh = logging.FileHandler('spam.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #创建格式化
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
    
    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)
    def war(self,message):
        self.logger.warning(message)
    def error(self,message):
        self.logger.error(message)
    def cri(self,message):
        self.logger.critical(message)
if __name__ == '__main__':
    l = Logger()
    l.info('hhhhh')
