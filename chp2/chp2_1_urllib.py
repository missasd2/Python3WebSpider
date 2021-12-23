import urllib.request

# response = urllib.request.urlopen("https://www.python.org")
# #print(response.read().decode("utf-8"))

# # <class 'http.client.HTTPResponse'>
# print(type(response))

# """
# HTTPResponse对象
# """
# print(response.status) # 200
# #print(response.getheaders()) # [('Connection', 'close'), ('Content-Length', '49809'), ('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'DENY'), ('Via', '1.1 vegur, 1.1 varnish, 1.1 varnish'), ('Accept-Ranges', 'bytes'), ('Date', 'Thu, 23 Dec 2021 14:41:43 GMT'), ('Age', '886'), ('X-Served-By', 'cache-iad-kjyo7100024-IAD, cache-nrt18336-NRT'), ('X-Cache', 'HIT, HIT'), ('X-Cache-Hits', '5, 642'), ('X-Timer', 'S1640270503.373045,VS0,VE0'), ('Vary', 'Cookie'), ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]
# print(type(response.getheaders())) # <class 'list'>


# data参数
def request_with_data():
    # 将请求参数转化为 字节流编码格式的内容；也就是bytes类型
    # urlencode()函数转化为字符串，并指定编码格式为utf-8
    data = bytes(urllib.parse.urlencode({"name": "germey"}), encoding="utf-8")
    response = urllib.request.urlopen("https://www.httpbin.org/post", data=data)
    print(response.read().decode("utf-8"))


# timeout参数
def request_with_timeout():
    response = urllib.request.urlopen("https://www.httpbin.org/get", timeout=0.1)
    print(response.read()) # urllib.error.URLError: <urlopen error timed out>
    pass


# 通过超时时间，跳过对网页的抓取
def skip_by_timeout():
    import socket
    import urllib.request
    import urllib.error
    try:
        response = urllib.request.urlopen("https://www.httpbin.org/get", timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("TIME OUT")

if __name__ == "__main__":
    # request_with_timeout()
    skip_by_timeout()