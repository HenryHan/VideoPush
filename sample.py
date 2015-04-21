import lib.publisher
import os
USERNAME = ''
PASSWORD = ''
data_file = os.getcwd() + "/config/dota.ini"
log_file = os.getcwd() + "/logs/dota.txt"
lib.publisher.publish_main(data_file,log_file)