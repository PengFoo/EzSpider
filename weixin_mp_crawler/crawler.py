# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
import sys


__author__ = 'fupeng'


reload(sys)
sys.setdefaultencoding('utf8')
'''
global varibles
'''
accounts = []
accounts_file_name = './weixin_accouts.txt'
proxyIp = []


'''
get proxy ips from the txt file
'''
def handleProxy():
    with open('proxy.txt', 'r') as f:
        for line in f:
            ip = line.strip().split('@')[0]
            proxyIp.append(ip)

# weixin media platform accounts
# should be 2 column
# mp_name \t mp_account
def loadWeixinAccounts(fileName):
    with open(fileName, 'r') as f:
        for line in f:
            _, mp_account = line.replace('\n', '').split('\t')
            if mp_account != '':
                accounts.append(mp_account)


# loadWeixinAccounts('weixin_accouts.txt')


def crawlMpId():
    for account in accounts:
        payload = {}
        headers = {}
        payload['q'] = account
        payload['search_field'] = 2

        req = requests.get('http://www.gsdata.cn/query/wx', params=payload, headers=headers)
        req.encoding = 'utf-8'

        if 'API接口免费申请开' in req.text:
            print 'done'
        else:
            print 'yes'
            # dom = pq(req.text)
            # idDom = pq(dom('.wxgzh')[0])
            # idHref = idDom('.gzh_t a').attr('href')

            # print account, idHref


loadWeixinAccounts('weixin_accouts.txt')
crawlMpId()




'''
just for test
'''
def testRecentArticle():
    payload = {}
    payload['type'] = 'recently'
    payload['id'] = 24
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Referer': 'http://www.gsdata.cn/rank/single/24',
        'X-Requested-With': 'XMLHttpRequest'}

    req = requests.get('http://www.gsdata.cn/index.php/rank/recommendArticles', params=payload, headers=headers)
    print req.text
    print req.json()['result']['items'][0]['name']


'''
just for test
'''


def testSearch():
    payload = {}
    headers = {}

    payload['q'] = '澎湃新闻'
    req = requests.get('http://www.gsdata.cn/query/wx', params=payload, headers=headers)

    req.encoding = 'utf-8'
    print req.text

# testRecentArticle()   succeed
# testSearch()          succeed
