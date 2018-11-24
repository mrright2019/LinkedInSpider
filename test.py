#coding:utf-8
import copy
from bs4 import BeautifulSoup
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf8')
from Config import *
from urllib import quote


client_s = requests.Session()
client_s.headers = headers
client_s.verify = False

def login(laccount, lpassword):
    login_res = client_s.get('https://www.linkedin.com/uas/login')
    login_soup = BeautifulSoup(login_res.content,"html.parser")
    login_csrf = login_soup.find("input",attrs={"id":"loginCsrfParam-login"})['value']
    login_csrf_token = login_soup.find("input",attrs={"id":"csrfToken-login"})['value']
    login_alias = login_soup.find("input",attrs={"id":"sourceAlias-login"})['value']
    login_sign_in = login_soup.find("input",attrs={"name":"signin"})['value']
    data = {
        'isJsEnabled': "true",
        'source_app': "",
        'tryCount': "tryCount",
        'clickedSuggestion': "false",
        'session_redirect': "",
        'trk': "",
        'fromEmail': "",
        'session_key': laccount,
        'session_password': lpassword,
        'signin': login_sign_in,
        'loginCsrfParam': login_csrf,
        'csrfToken': login_csrf_token,
        'sourceAlias': login_alias
    }
    # print data
    client_s.post('https://www.linkedin.com/uas/login-submit', data=data)





def search_keyword_page(keyword,page=1):
    if page<=1:
        s_u = search_url+quote(keyword)
    else:
        s_u = search_url+quote(keyword)+"&page="+str(page)
    print s_u
    search_res = client_s.get(s_u)
    search_res_soup = BeautifulSoup(search_res.content,"html.parser")
    # print search_res.content
    search_res_list = search_res_soup.find_all("code")[code_num_of_json]
    jsonstr = search_res_list.get_text()
    jsondata = json.loads(jsonstr)
    for now_data in jsondata['included']:
        if now_data.has_key("firstName"):
            print "firstName:",now_data['firstName']
        if now_data.has_key("lastName"):
            print "lastName:",now_data['lastName']
        if now_data.has_key("occupation"):
            print "occupation:",now_data['occupation']
        if now_data.has_key("publicIdentifier"):
            print "publicIdentifier:",now_data['publicIdentifier']
        print "---------------------------------------------------------------------------------------"
        print "---------------------------------------------------------------------------------------"



def search(keyword):
    for i in range(1,100):
        search_keyword_page(keyword,page=i)
        time.sleep(3)


def loop():
    for k in keywords:
        search("建筑")

if __name__ == "__main__":
    login(username,password)
    res = client_s.get("https://www.linkedin.com/feed/?trk=")
    loop()