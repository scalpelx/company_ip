import requests
from bs4 import BeautifulSoup

def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('IP: ' + ip)
    return ip

def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,"html.parser").iframe
    return soup["src"]

if __name__ == '__main__':
    get_out_ip(get_real_url())
