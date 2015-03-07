import time
import os
import weibocontroller as weibo
import youkucontroller as youku
import __main__ as main

def publish_youku_to_weibo():
    authors = get_authors(main.AUTHORS)
    while True:
        write_log("start to check")
        for author in authors: 
            try:
                links = youku.get_video_from_lib(author[1])
            except Exception,e:
                write_log(e.message)
            else:
                for link in links:
                    if link['time'] > author[2]:
                        try:
                            weibo.publish(link['title'] + ': '+link['link'])
                        except Exception,e:
                            write_log(e.message)
                        else:
                            author[2] = link['time']
                            write_log("publish "+link['title']+" "+link['link'])
            time.sleep(30)
        write_log("end of publishment")
        update_authors(authors)
        time.sleep(main.INTERVAL)
    
def get_authors(authors):
    if os.path.exists(main.DATAPATH):
        authors = read_list(main.DATAPATH)
    return authors
def update_authors(authors):
    write_list(authors)
def write_list(list):
    f = open(main.DATAPATH,"w")
    for l in list:
        f.write(l[0]+','+l[1]+','+l[2]+'|')
    f.close
def read_list(datapath):
    f = open(datapath,"r")
    l = f.readline()
    authors = l.split("|")
    list = []
    for a in authors:
        author = a.split(',')
        if len(author) == 3:
            list.append(author)
    f.close
    return list

def write_log(content):
    log = open(main.LOGPATH,"a")
    log.write(now() + content+"\r\n")
    log.close
def now():
    return time.strftime('[%Y-%m-%d %H:%M:%S] ',time.localtime(time.time()))
