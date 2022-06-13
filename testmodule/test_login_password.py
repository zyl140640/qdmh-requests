# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/5/16 09:41
@file: test_login_password.py
@desc: 
"""
import logging

import allure
import pytest

from common.assert_util import response_body_check
from common.public_function import *
from common.request_util import *
from common.yaml_util import *


@allure.feature("账号模块")
class TestLoginPassword:

    def setup_class(self):
        self.req = RequestHandler()
        self.logger = logging

    @allure.story("登录")
    @pytest.mark.parametrize('args', case_yaml('login_password.yaml'))
    def test_login_password(self, args):
        url = get_url(args.get('url'))
        payload = args.get('body')
        token = read_yaml_key('config/config.yaml', 'token')
        headers = request_header(payload, token)
        response = self.req.visit("POST", url, headers=headers, json=payload)
        response_body_check(args, response)