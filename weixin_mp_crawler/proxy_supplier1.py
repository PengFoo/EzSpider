import sys
sys.path.append("..")

from ezspider.proxy import proxy
from pyquery import PyQuery as pq
import requests
from multiprocessing import freeze_support


url = 'http://www.youdaili.net/Daili/http/'


def getProxIps():
    r = requests.get(url)
    r.encoding = 'utf-8'
    dom = pq(r.text)

    ipListUrl = pq(dom('.newslist_line a')[0]).attr('href')

    r = requests.get(ipListUrl)
    r.encoding = 'utf-8'
    dom = pq(r.text)

    pages = dom('.dede_pages li>a')
    pageCount = len(pages) - 3

    for i in range(1, pageCount+1):
        if i == 1:
            ipUrl = ipListUrl
        else:
            ipUrl = ipListUrl.split('.html')[0] + '_' + str(i) + '.html'
        r = requests.get(ipUrl)
        r.encoding = 'utf-8'

        dom = pq(r.text)
        # $('.cont_font p')
        ips = dom('.cont_font p').html()
        # 1.207.62.194:3128@HTTP#place
        for line in ips.split('\n'):
            ip = line.split('@')[0]
            print ip
            proxy.addProxyIpAsync(ip)


if __name__ == '__main__':
    proxy.init()
    getProxIps()
    proxy.wait()
