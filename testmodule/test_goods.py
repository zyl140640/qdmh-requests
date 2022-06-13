import allure
import pytest
from jsonschema import validators
from common.assert_util import *
from common.public_function import *
from common.yaml_util import *


@allure.feature("商品模块")
class TestGoods:
    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("商品详情")
    @allure.title("验证商品详情是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_details.yaml'))
    def test_goods_details(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品收藏")
    @allure.title("验证收藏商品是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_favorite.yaml'))
    def test_goods_favorite(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品评论")
    @allure.title("验证商品评论是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_comments.yaml'))
    def test_goods_comments(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品相关推荐")
    @allure.title("验证相关推荐是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_recommend.yaml'))
    def test_goods_recommend(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品二维码")
    @allure.title("验证商品二维码是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_qrcode.yaml'))
    def test_goods_qrcode(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品优惠价")
    @allure.title("验证商品优惠价是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_promo.yaml'))
    def test_goods_promo(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品库存量")
    @allure.title("验证商品库存量是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_inventory.yaml'))
    def test_goods_inventory(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品专题下的分类")
    @allure.title("验证专题下的分类是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_recommend_category.yaml'))
    def test_goods_recommend_category(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品专题分类商品")
    @allure.title("验证商品专题分类商品是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_recommend_details.yaml'))
    def test_goods_recommend_details(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("商品收藏/关注列表")
    @allure.title("验证商品收藏/关注列表是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_favorite_list.yaml'))
    def test_goods_favorite_list(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("最近7天")
    @allure.title("验证最近7天是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_days.yaml'))
    def test_goods_days(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("当天商品历史")
    @allure.title("验证当天商品历史是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_visit.yaml'))
    def test_goods_visit(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("降价通知")
    @allure.title("验证降价通知是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('goods_depreciate.yaml'))
    def test_goods_depreciate(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)


