
import sys
sys.path.append("..")

from ezspider.proxy import proxy
from pyquery import PyQuery as pq
import requests
from multiprocessing import freeze_support


url = 'http://www.haodailiip.com/domftiqu?country=%E5%85%A8%E9%83%A8&region=%E5%85%A8%E9%83%A8&city=%E5%85%A8%E9%83%A8&number=50&anonType=-1&proxyType=-1&ispId=-1'


def getProxIps():
    r = requests.get(url)
    r.encoding = 'utf-8'
    dom = pq(r.text)
    ipList = dom('p')
    for i in ipList:
        ip = pq(i).html()
        if ip:
            proxy.addProxyIpAsync(ip)


if __name__ == '__main__':
    proxy.init()
    getProxIps()
    proxy.wait()
