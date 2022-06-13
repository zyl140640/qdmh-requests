# # encoding: utf-8
# """
# @author: 宋坤坤
# @contact: cailyn.song@isysful.com
# @time: 2022/5/17 15:19
# @file: test_address_remove.py
# @desc:
# """
# import json
# import logging
#
# import allure
# import pytest
# from jsonschema import validators
# from common.public_fun import *
# from common.request_util import *
# from common.yaml_util import *
#
#
# @allure.feature("地址模块")
# class TestAddressRemove:
#
#     def setup_class(self):
#         self.req = RequestHandler()
#         self.logger = logging
#
#     @allure.story("移除地址")
#     @pytest.mark.parametrize('args', case_yaml('address_remove.yaml'))
#     def test_address_remove(self, args):
#         url = get_url(args.get('url'))
#         payload = args.get('body')
#         token = read_yaml_key('config/config.yaml', 'token')
#         headers = request_header(payload, token)
#         response = self.req.visit("POST", url, headers=headers, json=payload)
#         schema = args.get('schema')
#         va = validators.Draft4Validator(schema)
#         va.validate(response.json())
#         logging.info(json.dumps(response.json()))
#         print(response.json())
#         return response.json()
