#coding=utf-8

import logging
import time

#第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)#Log等级开关



#第二步，创建一个handler,用于写入日志文件
#now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
logfile = "./log.txt"

fh = logging.FileHandler(logfile,mode='a',encoding='utf-8') #open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG) #输出到file的log等级

#第三步，再创建一个handler,用于输出到一个控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关


#第四步：定义handleer的输出模式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#第五步:将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

#日志
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')