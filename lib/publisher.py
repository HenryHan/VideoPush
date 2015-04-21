# -*- coding:utf-8 -*-
import ConfigParser
import hlog
import youkucontroller as youku
import os
import time
import weibocontroller as weibo

def publish_main(data_file,log_file):
    count = 0
    history_count = 0
    while True:
        try:
            h = hlog.hlog(log_file)
            h.write_info("start to publish")
            config = ConfigParser.ConfigParser()
            config.readfp(open(data_file,'rb'))
            authors = config.sections()
            for index, author in enumerate(authors):
                p = publisher(data_file,author)
                if p.get_last() != "":

                    try:
                        weibo.publish(p.get_last())
                    except Exception,e:
                        h.write_error(e.message)
                    else:
                        count = 0
                        h.write_info(p.get_last())
                if count > 4 and history_count%len(authors) == index:
                    try:
                        weibo.publish(p.get_history())
                    except Exception,e:
                        h.write_error(e.message)
                    else:
                        h.write_info(p.get_history())
                        count = 0
                        history_count = history_count + 1
            count = count + 1
            h.write_info("end of publishment")
        except Exception, ee:
            pass
        time.sleep(3600)

class publisher():
    name = ''
    link = ''
    last_update = ''
    last_history = ''
    file_path = ''
    def __init__(self,file_path,name):
        self.name = name
        self.file_path = file_path
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.file_path,'rb'))
        self.link = config.get(name,"link")
        self.last_update = config.get(name,"last_update")
        self.last_history = config.get(name,"last_history")
    def set_update(self,update):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.file_path,'rb'))
        config.set(self.name,"last_update",update)
        config.write(open(self.file_path,'wb'))
    def set_history(self,history):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.file_path,'rb'))
        config.set(self.name,"last_history",history)
        config.write(open(self.file_path,'wb'))
    def get_last(self):
        last = ''
        try:
            links = youku.get_video_from_lib(self.link)
        except Exception,e:
            return last
        else:
            for link in links:
                if link['time'] > self.last_update:
                    self.set_update(link['time'])
                    last = link['title'] + ': '+link['link']
                    return last
            return last
    def get_history(self):
        history = ''
        i = 1
        while i < 11:
            try:
                links = youku.get_video_from_lib(self.link + "/fun_ajaxload/?__rt=1&__ro=&v_page=1&page_num="+str(i)+"&page_order=1&q=&last_str=")
            except Exception,e:
                return history
            else:
                for link in links:
                    if link['time'] < self.last_history:
                        self.set_history(link['time'])
                        history = "【精彩回顾】" + link['title'] + ': '+link['link']
                        return history
            i = i + 1
        return history