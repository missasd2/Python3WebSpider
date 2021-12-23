"""
Request
"""


def example_request():
    from urllib import  parse, request
    # 通过参数构建 request对象
    url = "https://www.httpbin.org/post"
    dict = {"name":"germey"}
    data=bytes(parse.urlencode(dict), encoding="utf-8")
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "Host": "www.httpbin.org"
    }
    method="POST"
    req = request.Request(url=url, data=data, headers=headers, method=method
    )
    response = request.urlopen(req)
    print(response.read().decode("utf-8"))
    


if __name__ == "__main__":
    # request_with_timeout()
    print()
    example_request()