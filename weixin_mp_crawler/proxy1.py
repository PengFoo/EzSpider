import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')
url = 'http://www.gsdata.cn/query/wx?q=ttt'
proxyIp = []


def handleProxy():
    with open('p.txt', 'r') as f:
        for line in f:
            ip = line.strip().split('\t')[0] + ':' + line.strip().split('\t')[1]
            proxyIp.append(ip)


if __name__ == '__main__':
    handleProxy()
    print proxyIp
    for ip in proxyIp:
        proxy = {'http': ip}
        r = requests.session()
        try:
            response = r.get(url, proxies=proxy)
            print proxy, response.status_code
        except Exception, e:
            print proxy, 'failed'
