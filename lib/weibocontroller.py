import __main__ as main
import httplib,urllib
from weibo import APIClient

def publish(content):
    client = APIClient(app_key=main.APP_KEY, app_secret=main.APP_SECRET, redirect_uri=main.CALLBACK_URL)
    url = client.get_authorize_url()
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode({'client_id':main.APP_KEY,'response_type':'code','redirect_uri':main.CALLBACK_URL,'action':'submit','userId':main.USERNAME,'passwd':main.PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url, 'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    page = res.read()
    location = res.msg.dict['location']
    conn.close()
    code = location[location.find("code=")+5:]
    r = client.request_access_token(code)
    client.set_access_token(r.access_token, r.expires_in)
    client.post.statuses__update(status=content)
        
    