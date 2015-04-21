import __main__ as main
import httplib,urllib
from weibo import APIClient

APP_KEY = '991876812' 
APP_SECRET = '60d0e3124af3e8246940e9abf0af8032' 
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' 

def publish(content):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':main.USERNAME,'passwd':main.PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url, 'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    page = res.read()
    location = res.msg.dict['location']
    conn.close()
    code = location[location.find("code=")+5:]
    r = client.request_access_token(code)
    client.set_access_token(r.access_token, r.expires_in)
    client.post.statuses__update(status=content)
        
    