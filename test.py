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
    client_s.post('https://www.linkedin.com/uas/login-submit', data=data)





def search_keyword_page(keyword,page=1):
    if page<=1:
        s_u = search_url+quote(keyword)
    else:
        s_u = search_url+quote(keyword)+"&page="+str(page)
    print s_u
    search_res = client_s.get(s_u)
    if search_res.status_code != 200:
        print u"网站可能有变更 或者账号被封"
        exit()
    search_res_soup = BeautifulSoup(search_res.content,"html.parser")
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




import threading
import Queue
class mythread(threading.Thread):
    _pagequeue = None
    _look = threading.Lock()
    def __init__(self,keyword): 
        threading.Thread.__init__(self)
        self.keyword = keyword
        self.set_pagequeue()

    @classmethod
    def set_pagequeue(self):
        self._look.acquire()
        if self._pagequeue is None:
            self._pagequeue = Queue.Queue()
            for i in range(0,200):
                self._pagequeue.put(i)
        self._look.release()

    @classmethod
    def get_pagequeue(self):
        self._look.acquire()
        if self._pagequeue.empty():
            res = -1
        else:
            res = self._pagequeue.get()
        self._look.release()
        return res

    def getpage(self):
        self._look.acquire()
        if self.pagequeue.qsize() == 0:
            res = -1
        else:
            res = self.pagequeue.get()
        self._look.release()
        return res

    def run(self):
        page = self.get_pagequeue()
        while page != -1:
            search_keyword_page(self.keyword,page)
            time.sleep(5)
            page = self.get_pagequeue()




if __name__ == "__main__":
    login(username,password)
    tasks = []
    for i in range(1):
        t = mythread("建筑")
        t.start()
        tasks.append(t)
    for t in tasks:
        t.join()