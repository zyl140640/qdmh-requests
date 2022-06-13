# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/11 17:47
@file: test_category.py
@desc: 分类模块的接口测试用例
"""

import logging

import allure
import pytest

from common.public_function import *
from common.yaml_util import *


@allure.feature("分类模块")
class TestCategory:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.title("验证商品主分类是否能请求通过")
    @allure.story("商品主分类")
    @pytest.mark.parametrize('args', case_yaml('category_mall.yaml'))
    def test_category_mall(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 商品主分类,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证商品主分类子项是否能请求通过")
    @allure.story("商品主分类子项")
    @pytest.mark.parametrize('args', case_yaml('category_items.yaml'))
    def test_category_items(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 商品主分类子项,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("餐饮商品分类")
    @allure.title("验证餐饮商品分类是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('category_cater.yaml'))
    def test_category_cater(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 餐饮商品分类,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("依分类显示餐饮商品")
    @allure.title("验证依分类显示餐饮商品是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('category_cater_dishes.yaml'))
    def test_category_cater_dishes(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 依分类显示餐饮商品,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("依分类显示超市商品")
    @allure.title("验证依分类显示超市商品是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('category_supermarket_dishes.yaml'))
    def test_category_supermarket_dishes(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 依分类显示超市商品,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("超市商品分类")
    @allure.title("验证超市商品分类是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('category_supermarket.yaml'))
    def test_category_supermarket(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 超市商品分类,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json
