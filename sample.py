import lib.mylib as mylib
import sys
path = sys.path[0]

APP_KEY = '' 
APP_SECRET = '' 
CALLBACK_URL = ''

LOGPATH = path + "/log/dota.log"
DATAPATH = path + "/data/dota.txt"
USERNAME = ''
PASSWORD = ''
INTERVAL = 3600
AUTHORS = [["","",""]
          ]

mylib.publish_youku_to_weibo()