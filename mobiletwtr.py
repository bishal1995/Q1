import requests
import time
from bs4 import BeautifulSoup
email = 'your_Email'
password = 'your_password'
loginUrl = 'https://mobile.twitter.com/login/'
ReqHeaders = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
loginRequest = requests.get(loginUrl,headers=ReqHeaders)
data = loginRequest.text
soup = BeautifulSoup(data)
authenticity_token = soup.find_all('meta')[4]['content']
redirect_after_login = soup.find_all('input')[3]['value']
_mb_tk = loginRequest.cookies['_mb_tk']  
_mobile_sess = loginRequest.cookies['_mobile_sess']
_twitter_sess = loginRequest.cookies['_twitter_sess']
guest_id = loginRequest.cookies['guest_id']
mobile_metrics_token = loginRequest.cookies['mobile_metrics_token']
zrca = loginRequest.cookies['zrca']
loginReqCookie = {
	'_mb_tk' : _mb_tk,
	'_mobile_sess' : _mobile_sess,
	'_twitter_sess' : _twitter_sess,
	'guest_id' : guest_id,
	'mobile_metrics_token' : mobile_metrics_token,
	'zrca' : zrca
}
loginReqPayload = {
	'authenticity_token' : authenticity_token,
	'remember_me':1,
	'wfa':1,
	'redirect_after_login':redirect_after_login,
	'session[username_or_email]':email,
	'session[password]':password
}
loginReqHeader = {
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en-GB,en-US;q=0.8,en;q=0.6',
	'cache-control':'max-age=0',
	'Content-Type':'application/x-www-form-urlencoded',
	'Origin':'https://mobile.twitter.com',
	'Referer':'https://mobile.twitter.com/login/',
	'Upgrade-Insecure-Requests':1,
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
}
# session generation url
sessionUrl = 'https://mobile.twitter.com/sessions/'
sessionRequest = requests.post(sessionUrl,headers=ReqHeaders,cookies=loginReqCookie,data=loginReqPayload)
print(sessionRequest.content)
print(sessionRequest.cookies)



















































































