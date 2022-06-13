import allure
import pytest

from common.assert_util import *
from common.public_function import *
from common.yaml_util import *


@allure.feature("账号模块")
class TestAccount:
    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("登录")
    @allure.title("验证登录是否能请求通过")
    @pytest.mark.parametrize('payload', case_yaml('login_password.yaml'))
    def test_login_password(self, payload):
        url = get_url(payload.get('url'))
        request_body = payload.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(request_body, token)
        response = self.req.visit("POST", url, headers=headers, json=request_body)
        schema = payload.get('schema')
        va = validators.Draft4Validator(schema)
        va.validate(response.json())
        logging.info(response.json())
        return response.json()

    @allure.story("注册")
    def account_register(self):
        url = get_url('/m/account/register')
        payload = {
            "login_id": "19953234212",
            "passwd": "648d92bbe20fbf01cc08c28b26efaca4",
            "type": 1,
            "vcode": "658750"
        }
        token = ''
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        return response_json

    @allure.story("找回密码")
    def account_forget(self):
        url = get_url('m/account/forgot')
        payload = {
            "login_id": "19953234212",
            "passwd": "648d92bbe20fbf01cc08c28b26efaca4",
            "passwd_new": "202cb962ac59075b964b07152d234b70",
            "service_code": "10",
            "request_type": 2,
            "type": "1"
        }

        token = ''
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_json = response.json()
        return response_json
