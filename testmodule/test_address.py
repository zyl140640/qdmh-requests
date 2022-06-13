import logging

import allure
import pytest
from jsonschema import validators
from common.assert_util import *
from common.public_function import *
from common.yaml_util import *


@allure.feature("收货地址")
class TestAddress:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("收货地址列表")
    @allure.title("验证收货地址列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('address_list.yaml'))
    def test_address_list(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("增加收货地址")
    @allure.title("验证增加收货地址是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('address_add.yaml'))
    def test_address_add(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        schema = args.get('schema')
        va = validators.Draft4Validator(schema)
        va.validate(response.json())
        logging.info(json.dumps(response.json()))
        # 更新address_edit.yaml文件里的address_id
        change_data_yaml('address_edit.yaml', 'body', 'address_id', response.json()['data']['address_id'])
        # 更新address_detail.yaml文件里的address_id
        change_data_yaml('address_detail.yaml', 'body', 'address_id', response.json()['data']['address_id'])
        # 更新address_remove.yaml文件里的address_id
        change_data_yaml('address_remove.yaml', 'body', 'address_ids', response.json()['data']['address_id'])
        return response.json()

    @allure.story("编辑收货地址")
    @allure.title("验证编辑收货地址是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('address_edit.yaml'))
    def test_address_edit(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)


    @allure.story("收货地址详情")
    @allure.title("验证收货地址详情是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('address_detail.yaml'))
    def test_address_detail(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("清除收货地址")
    @allure.title("验证清除收货地址是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('address_remove.yaml'))
    def test_address_remove(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)
