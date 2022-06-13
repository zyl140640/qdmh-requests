import allure
import pytest
from common.assert_util import *
from common.public_function import *
from common.yaml_util import *


@allure.feature("会员资料")
class TestMember:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("会员资料详情")
    @allure.title("验证会员资料详情是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('member_detail.yaml'))
    def test_member_get(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("会员资料修改")
    @allure.title("验证会员资料修改是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('member_modify.yaml'))
    def test_member_modify(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("会员中心信息")
    @allure.title("验证会员中心信息是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('member_center.yaml'))
    def test_member_center(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("会员卡商品信息")
    @allure.title("验证会员卡商品信息是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('member_vipCardInfo.yaml'))
    def test_member_vip(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)

    @allure.story("会员卡激活")
    @allure.title("验证会员卡激活是否能请求通过")
    @pytest.mark.parametrize('args', case_yaml('member_activate.yaml'))
    def test_member_activate(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)
