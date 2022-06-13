import logging

import allure
import pytest

from common.public_function import *
from common.request_util import *
from common.yaml_util import *


@allure.feature("搜索模块")
class TestSearch:
    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("搜索结果列表")
    @allure.title("验证搜索结果列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_query.yaml'))
    def test_search_query(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索结果列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("搜索热点列表")
    @allure.title("验证搜索热点列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_hot.yaml'))
    def test_search_hot(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索热点列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("搜索筛选列表")
    @allure.title("验证搜索筛选列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_filter.yaml'))
    def test_search_filter(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索筛选列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("搜索-猜你喜欢")
    @allure.title("验证搜索-猜你喜欢是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_liked.yaml'))
    def test_search_liked(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索-猜你喜欢,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("搜索框-输入响应数据")
    @allure.title("验证搜索框-输入响应数据是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_enter.yaml'))
    def test_search_enter(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索-输入响应数据,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("搜索框-占位符")
    @allure.title("验证搜索框-占位符是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_placeholder.yaml'))
    def test_search_placeholder(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.text
        logging.info('模块名称: 搜索-输入响应数据,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.story("瀑布流")
    @allure.title("验证瀑布流是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('search_page.yaml'))
    def test_search_page(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 搜索-瀑布流,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json
