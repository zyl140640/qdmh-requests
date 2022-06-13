from common.request_util import RequestHandler


def apifox():
    url = "https://api.apifox.cn/api/v1/login?locale=zh-CN"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN',
        'Access-Control-Allow-Origin': '*',
        'Authorization': '',
        'Connection': 'keep-alive',
        'Host': 'api.apifox.cn',
        'Origin': 'https://www.apifox.cn',
        'Referer': 'https://www.apifox.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'X-Client-Mode': 'web',
        'X-Client-Version': '2.1.18-alpha.3',
        'X-Device-Id': 'OuR7vV9c-eZjv-baBa-YYjY-TZiJ6cqCbNv5',
        'X-Project-Id': '489047',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    pa = {
        "account": "yuanlong.zhang",
        "password": "15533065391"
    }
    repoesen = req.visit(method="get", url=url, headers=headers, params=pa)
    return repoesen.json()


if __name__ == '__main__':
    req = RequestHandler()
    url = "https://api.apifox.cn/api/v1/api-details?locale=zh-CN"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN',
        'Access-Control-Allow-Origin': '*',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDM3Nzg4LCJ0cyI6ImQyMmE4ZTQ1ZDI0MGJkZTAiLCJpYXQiOjE2NTM2MjAxNDIxMTd9.BYUH2pX1AeCEHBvp14786Fvcm3FIb706YkmqFwF4KQE',
        'Connection': 'keep-alive',
        'Host': 'api.apifox.cn',
        'Origin': 'https://www.apifox.cn',
        'Referer': 'https://www.apifox.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'X-Client-Mode': 'web',
        'X-Client-Version': '2.1.18-alpha.3',
        'X-Device-Id': 'OuR7vV9c-eZjv-baBa-YYjY-TZiJ6cqCbNv5',
        'X-Project-Id': '489047',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Cookie': 'acw_tc=76b20f6416536202198792262e06be7407b85692c3d0eadc11244435372b80'
    }
    pa = {}

    rest = req.visit(method="get", url=url, headers=headers, params=pa)
    name = rest.json()['data']
    e = enumerate(name)
    for index, value in e:
        print('%s, %s' % (index, value))
