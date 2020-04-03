import requests

#khi khi da lan setting
port = '1081'
http_proxy = "http://127.0.0.1:%s"%port
https_proxy = "https://127.0.0.1:%s"%port
ftp_proxy = "ftp://127.0.0.1:%s" % port

#danh cho ai mua sock tren mang, thi se co them user va pass
# {"http": "http://user:pass@domain:port"


proxyDict = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy
}

res = requests.get('https://api6.ipify.org/?format=json', proxies=proxyDict)
kq = res.text
print(kq)
