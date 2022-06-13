# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/6 16:07
@file: test_carts.py
@desc: 
"""
import logging

import allure
import pytest

from common.public_function import *
from common.yaml_util import *


@allure.feature("购物车模块")
class TestCarts:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("查询购物车")
    @allure.title("验证查询购物车是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_merge.yaml'))
    def test_carts_merge(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 查询购物车,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("添加购物车")
    @allure.title("验证添加购物车是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_add.yaml'))
    def test_carts_add(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 添加购物车,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("清空购物车")
    @allure.title("验证清空购物车是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_add.yaml'))
    def test_carts_remove(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 清空购物车,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("购物车中根据店铺获取优惠券列表")
    @allure.title("验证购物车中根据店铺获取优惠券列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_coupon.yaml'))
    def test_carts_coupon(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 购物车中根据店铺获取优惠券列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("选中购物项")
    @allure.title("验证选中购物项是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_checked.yaml'))
    def test_carts_checked(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 选中购物项,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("购物车下单-token")
    @allure.title("验证购物车下单-令牌否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_gettoken.yaml'))
    def test_carts_gettoken(self, args):
        req = RequestHandler()
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        change_yaml('config/config.yaml', 'gettoken', response_json['data'])
        logging.info('模块名称: 购物车下单-令牌,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("购物车下单")
    @allure.title("验证购物车下单否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_orders.yaml'))
    def test_carts_orders(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 购物车下单,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("立即购买")
    @allure.title("立即购买是否请求通过")
    @pytest.mark.parametrize('args', case_yaml('carts_buy.yaml'))
    def test_carts_checked(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 立即购买,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json
