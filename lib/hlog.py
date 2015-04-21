import os
import time
class hlog():
    logpath = ''
    def __init__(self, path):
        self.logpath = path
        print os.getcwd()
        if not os.path.exists(path):
            f = open(path, 'a')
            f.close()
    def write(self, message, level):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        f = open(self.logpath, 'a')
        f.write('[%s] %s: %s\r\n' % (now, level, message))
        f.close
    def write_info(self,message):
        self.write(message,"INFO")
    def write_warning(self,message):
        self.write(message,"WARNING")
    def write_error(self,message):
        self.write(message,"ERROR")


