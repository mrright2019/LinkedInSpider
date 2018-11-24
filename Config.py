#coding:utf-8
headers = {
	'Host': 'www.linkedin.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Connection': 'keep-alive',
	#'Cookie: JSESSIONID="ajax:5174229912088936307"; bcookie="v=2&3075de62-ddab-45d0-8d56-597987d22569"; bscookie="v=1&20181123084246b6a38818-4d07-4cbe-8d25-3869bae65999AQGN5C_xewqOIU1k12uqgj--mnhMYeCc"; lidc="b=SGST01:g=3:u=1:i=1543030129:t=1543116529:s=AQGeNXidnJhRncP5bUoMCDNk03H_FVXp"; fid=AQFo1J4Kina5xQAAAWc_xEvmOkGQSJ6HKWDWQQfaa5sJ5qEwSqckTvkbKLmsgIb06wbnXrOcgu6Qzg; visit="v=1&M"; _lipt=CwEAAAFnP9WwCyjZki9_kFKJuL19D8AlR9QNosGInSPH6tRXU070Sc3vjq6Q-_p0HCqqpE0VXNLSX_I0iZx2xjfV1jSpWKKEbCSeqqr-ocHuy7XMnR_FeHadVMAr_9vbvDbL_Y9tvZYpAg; UserMatchHistory=AQK2GtG57i1MlwAAAWc_xWaHg9wBTfW5A_UwTQ0oSoj2tleyqR29x6Wqp9mz-cu4GmHWVJEF_sF7qNjYA2092wVh0QxsDaU-dSK02rV4L0bZ6IlhBgNrAqYl5K0tORqN5GlNkQ; li_oatml=AQHYxuOUGeqzvgAAAWc_vo3bNDZ2UqcBgsv_w8FBU_8kjroQWd6MwyYhznXHZde9Drti67YJH3pC-P1CwJrhjNP7mbwYRve-; _guid=e3209dcc-b8a6-4f4d-9d8b-4724c19657fb; org_tcphc=true; lang="v=2&lang=zh-cn"; leo_auth_token="GST:9zXLCf62NqQBlhi0X1nfQresJBQCHhaQRTFLTMELNolwJyb6n0sxib:1543030400:e7fa0268bfffc7c320e9d9cda011de0c0cb4074a"
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0',
}

headers2 = {
	'Host': 'www.linkedin.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.linkedin.com/',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '123',
	'Connection': 'keep-alive',
	#Cookie: JSESSIONID="ajax:7582297873196655224"; bcookie="v=2&3075de62-ddab-45d0-8d56-597987d22569"; bscookie="v=1&20181123084246b6a38818-4d07-4cbe-8d25-3869bae65999AQGN5C_xewqOIU1k12uqgj--mnhMYeCc"; lidc="b=SGST01:g=3:u=1:i=1543043219:t=1543129619:s=AQERdNI7mtOZeZoPpBqJNA7ICcDpAywf"; fid=AQFo1J4Kina5xQAAAWc_xEvmOkGQSJ6HKWDWQQfaa5sJ5qEwSqckTvkbKLmsgIb06wbnXrOcgu6Qzg; visit="v=1&M"; _lipt=CwEAAAFnP9WwCyjZki9_kFKJuL19D8AlR9QNosGInSPH6tRXU070Sc3vjq6Q-_p0HCqqpE0VXNLSX_I0iZx2xjfV1jSpWKKEbCSeqqr-ocHuy7XMnR_FeHadVMAr_9vbvDbL_Y9tvZYpAg; UserMatchHistory=AQK2GtG57i1MlwAAAWc_xWaHg9wBTfW5A_UwTQ0oSoj2tleyqR29x6Wqp9mz-cu4GmHWVJEF_sF7qNjYA2092wVh0QxsDaU-dSK02rV4L0bZ6IlhBgNrAqYl5K0tORqN5GlNkQ; li_oatml=AQHYxuOUGeqzvgAAAWc_vo3bNDZ2UqcBgsv_w8FBU_8kjroQWd6MwyYhznXHZde9Drti67YJH3pC-P1CwJrhjNP7mbwYRve-; _guid=e3209dcc-b8a6-4f4d-9d8b-4724c19657fb; org_tcphc=true; lang="v=2&lang=zh-cn"; leo_auth_token="GST:9v0yieuEFCmPBZNsAeKyMePcjQmpNle3ShkrlBDKazCF-iNzZmx6yj:1543042126:cca7702219310cead7392fcb54ecc8bd105cf701"
	'Upgrade-Insecure-Requests': '1',
}


import execjs

def CreateGuid():
	with open('createguid.js') as fp:
		js = fp.read()
		ect = execjs.compile(js)
		# guid = ect.call('createGuid')
		guid = ect.call('createGuid') + ect.call('createGuid') + "-" + ect.call('createGuid') + "-" + ect.call('createGuid')+"-" + ect.call('createGuid') + "-" + ect.call('createGuid') + ect.call('createGuid') + ect.call('createGuid')
		return guid



username = "17865313385"
password = "Sunjinhua123"


search_url = "https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&keywords="


keywords = ["建筑","计算机"]

code_num_of_json = 16
