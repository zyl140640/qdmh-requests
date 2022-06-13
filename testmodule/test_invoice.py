# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/5/13 10:43
@file: test_invoice.py
@desc: 
"""

import allure
import pytest

from common.assert_util import *
from common.public_function import *
from common.yaml_util import *


@allure.feature("发票")
class TestInvoice:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("发票抬头列表")
    @allure.title("验证发票抬头列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('invoice_list.yaml'))
    def test_invoice_list(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 发票抬头列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("发票详情")
    @allure.title("验证发票详情是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('invoice.yaml'))
    def test_invoice(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 发票详情,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("添加发票抬头")
    @allure.title("验证添加发票抬头是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('invoice_add.yaml'))
    def test_invoice_add(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 添加发票抬头,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("编辑发票抬头")
    @allure.title("验证编辑发票抬头是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('invoice_edit.yaml'))
    def test_invoice_edit(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 编辑发票抬头,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("清除发票抬头")
    @allure.title("验证清除发票抬头是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('invoice_edit.yaml'))
    def test_invoice_remove(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 清除发票抬头,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json
