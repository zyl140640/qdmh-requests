import logging

import allure
import pytest

from common.public_function import *
from common.request_util import *
from common.yaml_util import *


@allure.feature("店铺模块")
class TestShop:
    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.title("店铺详情")
    @allure.story("店铺详情")
    @pytest.mark.parametrize('args', case_yaml('shop_details.yaml'))
    def test_shop_details(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺详情,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证收藏店铺是否能请求通过")
    @allure.story("收藏店铺")
    @pytest.mark.parametrize('args', case_yaml('shop_favorite.yaml'))
    def test_shop_favorite(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 收藏店铺,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证店铺自定义分类是否能请求通过")
    @allure.story("店铺自定义分类")
    @pytest.mark.parametrize('args', case_yaml('shop_category.yaml'))
    def test_shop_category(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺自定义分类,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证店铺中领券是否能请求通过")
    @allure.story("店铺中领券")
    @pytest.mark.parametrize('args', case_yaml('shop_coupon.yaml'))
    def test_shop_coupon(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺领券,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证店铺商品列表是否能请求通过")
    @allure.story("店铺商品列表")
    @pytest.mark.parametrize('args', case_yaml('shop_goods_list.yaml'))
    def test_shop_goods_list(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺商品列表,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证店铺证件照是否能请求通过")
    @allure.story("店铺证件照")
    @pytest.mark.parametrize('args', case_yaml('shop_license.yaml'))
    def test_shop_license(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺证件照,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json

    @allure.title("验证店铺二维码是否能请求通过")
    @allure.story("店铺二维码")
    @pytest.mark.parametrize('args', case_yaml('shop_qrcode.yaml'))
    def test_shop_qrcode(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml('config/config.yaml')['token']
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        logging.info('模块名称: 店铺二维码,测试目的: {} ,响应结果: {}'.format(args.get('case_name'), response_json))
        return response_json
