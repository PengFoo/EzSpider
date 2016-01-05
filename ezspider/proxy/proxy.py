from __future__ import absolute_import
import requests
import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool
import sys
import time

__author__ = 'peng foo'

'''
global variables
'''
p = None  # pool
curProcessNum = 0
initialized = False
proxyIpList = []  # proxy ips available
proxySupplier = []
testUrl = 'http://www.gsdata.cn/query/wx?q=test'


def init():
    global initialized, p, q
    if not initialized:
        p = Pool(50)
        initialized = True


def addProxyIps(ipList):
    for ip in ipList:
        addProxyIpAsync(ip)


def addProxyIpAsync(ip):
    '''
    using multiprocessing pool to
    test and add the proxy ip
    :param ip: a 'ip:port' formatted string
    :return: null
    '''
    global curProcessNum
    curProcessNum += 1
    p.apply_async(addProxyIp, args=(ip,), callback=processNumCallback)


def addProxyIp(ip):
    '''
    test if the ip is available,
    and add into the proxyIpList
    :param ip: a 'ip:port' formatted string
    :return: null
    '''
    global curProcessNum
    r = requests.session()
    proxy = {'http': str(ip)}
    try:
        if r.get(testUrl, proxies=proxy).status_code == 200:
            print ip, 'added!--------------'
            sys.stdout.flush()
            proxyIpList.append(ip)
    except Exception, e:
        print e.message
        print ip, 'failed!'
        sys.stdout.flush()


def processNumCallback(c):
    global curProcessNum
    curProcessNum -= 1


def wait():
    global curProcessNum
    while 1:
        time.sleep(10)
        print 'current process left', str(curProcessNum)
        if curProcessNum == 0:
            return
