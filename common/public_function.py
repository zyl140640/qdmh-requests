import json
import os
import random
import yaml
from common.request_util import RequestHandler
from common.yaml_util import read_yaml_key, get_object_data_path


# 拼接url
def get_url(path):
    """
    :param path: 请求接口路径
    :return: 返回完整的接口Url
    """
    url = read_yaml_key('config/config.yaml', 'baseURL') + path
    return url


# 获取header
def get_headers(request_body):
    """
    :param request_body: 请求接口的参数-Body
    :return:  返回Sign和时间戳
    """
    req = RequestHandler()
    get_sign_url = read_yaml_key('config/config.yaml', 'get_sign_url')
    url = get_url(get_sign_url)
    payload = request_body
    headers = read_yaml_key('config/config.yaml', 'headers')
    response = req.visit("POST", url, headers=headers, json=payload)
    response_json = response.json()
    return response_json


# 封装请求头，payload是请求体
def request_header(payload, token):
    """
    :param payload: 请求接口的Body
    :param token: 用户的令牌(Token)
    :return: 返回请求接口Body的完整信息
    """
    # 调用该方法时，传入请求体和token参数即可
    eqid = str(random.randint(100000, 2000000))
    body = get_headers(payload)
    headers = {
        'Authorization': 'MTIzOnJvb3Q=',
        'eqId': eqid,
        'Timestamp': json.dumps(body['data']['time_stamp_sys']),
        'Sign': body['data']['sign'],
        'Content-Type': 'application/json',
        'Access-Token': token
    }
    return headers


def yaml_case_data():
    """
    方法注解: 用于读取指定目录下的所有文件和子目录内的文件内容
    :return: 返回List类型的测试数据
    """
    # 定义路径
    path = os.getcwd() + read_yaml_key('config/config.yaml', 'case_data_path')
    # 设置空列表
    file_list = []
    yaml_list = []
    # 使用os.walk获取文件路径及文件
    for home, dirs, files in os.walk(path):
        # 遍历文件名
        for filename in files:
            # 将文件路径包含文件一同加入列表
            file_list.append(os.path.join(home, filename))
    # 赋值
    for i in file_list:
        args = case_yaml(i)
        for n in args:
            yaml_list.append(n)
    return yaml_list


def case_yaml(path):
    """
    读取config.yaml内case_data_path地址,进行测试路径拼接,用于pytest参数化方法
    :param path: 接口对应的Yaml测试数据文件地址
    :return: 返回Yaml内的List类型测试数据
    """
    # paths = read_yaml_key('config/config.yaml', 'case_data_path')
    # splicing_path = os.getcwd() + paths + path
    splicing_path = path
    with open(splicing_path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


def change_data_yaml(path, json1, json2, data):
    """
    用于修改指定YAML文件内list内参数值
    :param path: yaml文件名字
    :param json1: 数据体第一层的关键字
    :param json2: 第二层
    :param data: 修改后值
    """
    with open(get_object_data_path(path), encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        value[0][json1][json2] = data
    with open(get_object_data_path(path), mode='w', encoding='utf-8') as f:
        # 将Python中的字典或者列表转化为yaml格式的数据
        yaml.dump(value, f, allow_unicode=True, sort_keys=False)
        f.close()
