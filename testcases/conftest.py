# import logging
#
# import pytest
#
# from common.public_function import *
# from common.request_util import *
# from common.yaml_util import *
#
#
# @pytest.fixture(scope="session", autouse=True)
# @allure.story("账号密码登录更新token")
# def test_update_token():
#     path = read_yaml('data/single_data_v1.0/login/login_password.yaml')
#     req = RequestHandler()
#     url = get_url(path[0]['url'])
#     payload = path[0]['body']
#     token = ''
#     headers = request_header(payload, token)
#     response = req.visit("POST", url, headers=headers, json=payload)
#     response_json = response.json()
#     change_yaml('config/config.yaml', 'token', response_json['data']['token'])
#     assert response_json['msg'] == 'success', '请求失败,接口响应结果是: ' + response_json['msg']
#     return token
#
#
# @pytest.fixture(scope="session", autouse=True)
# @allure.story("更新购物车下单的gettoken")
# def test_carts_gettoken():
#     path = read_yaml('data/single_data_v1.0/carts/carts_gettoken.yaml')
#     req = RequestHandler()
#     url = get_url(path[0]['url'])
#     payload = path[0]['body']
#     token = read_yaml('config/config.yaml')['token']
#     headers = request_header(payload, token)
#     response = req.visit("POST", url, headers=headers, json=payload)
#     response_json = response.json()
#     change_data_yaml('carts/carts_orders.yaml', 'body', 'order_token', response_json['data'])
#     return response_json
#
#
# @pytest.fixture(scope="package", autouse=True)
# @allure.feature("设备")
# @allure.story("设备注册")
# def test_device_register():
#     path = read_yaml_key('config/config.yaml', 'device_register_url')
#     eqid = str(random.randint(100000, 2000000))
#     user_agent = read_yaml_key('config/config.yaml', 'User-Agent')
#     print(user_agent)
#     req = RequestHandler()
#     url = get_url(path)
#     payload = {}
#     token = ''
#     body = get_headers(payload)
#     headers = {
#         'Authorization': 'MTIzOnJvb3Q=',
#         'eqId': eqid,
#         'Timestamp': json.dumps(body['data']['time_stamp_sys']),
#         'Sign': body['data']['sign'],
#         'Content-Type': 'application/json',
#         'Access-Token': token,
#         'User-Agent': str(user_agent)
#     }
#     response = req.visit("POST", url, headers=headers, json=payload)
#     response_json = response.json()
#     assert response_json['msg'] == 'success' and response_json['code'] == 0
#     return response_json
#
#
# @pytest.fixture(scope="package", autouse=True)
# @allure.feature("设备")
# @allure.story("设备签到")
# def test_device_sign():
#     path = read_yaml_key('config/config.yaml', 'device_sign_url')
#     eqid = str(random.randint(100000, 2000000))
#     user_agent = read_yaml_key('config/config.yaml', 'User-Agent')
#     print(user_agent)
#     req = RequestHandler()
#     url = get_url(path)
#     payload = {}
#     token = ''
#     body = get_headers(payload)
#     headers = {
#         'Authorization': 'MTIzOnJvb3Q=',
#         'eqId': eqid,
#         'Timestamp': json.dumps(body['data']['time_stamp_sys']),
#         'Sign': body['data']['sign'],
#         'Content-Type': 'application/json',
#         'Access-Token': token,
#         'User-Agent': str(user_agent)
#     }
#     response = req.visit("POST", url, headers=headers, json=payload)
#     response_json = response.json()
#     assert response_json['msg'] == 'success' and response_json['code'] == 0
#     return response_json
