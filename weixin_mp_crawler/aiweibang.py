# -*- coding: utf-8 -*-

import sys
import requests
from pyquery import PyQuery as pq

reload(sys)
sys.setdefaultencoding('utf8')

urlToWrite = []

url = 'http://top.aiweibang.com/search/'

i = 0


def getUrl(name, account):
    global i
    _url = url + account
    req = requests.get(_url)

    req.encoding = 'utf-8'
    # print req.text
    dom = pq(req.text)

    id = dom('.wx-name a').attr('href')
    if id is  None:
        print name, account
        return '', '', '', ''


if __name__ == '__main__':
    file = open('weixin_accounts_20151230.txt', 'w+')
    with open('weixin_accouts.txt') as f:
        for line in f:
            _, account = line.replace('\n', '').split('\t')
            if account != '':
                getUrl(_, account)

    print i
    file.close()
