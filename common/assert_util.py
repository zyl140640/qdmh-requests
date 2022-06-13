# 接口返回的断言封装
import logging

import jsonschema
from jsonschema import validators


# args是从yaml文件读取的数据，response是接口返回的数据
def response_body_check(args, response):
    """
    用于校验接口的响应结果格式
    :param args: yaml文件读取的数据
    :param response: 接口返回的数据
    :return:  响应内容
    """
    try:
        # 首先打印接口返回参数，接口报错时可查看
        response_json = response.json()
        logging.info(response_json)
        # 获取yaml文件预期schema
        expect_schema = args.get('schema')
        # 获取yaml文件里用例名称
        case_name = args.get('case_name')
        # 判断返回msg
        assert response_json['msg'] == 'success', logging.error("模块名称: {},响应体断言结果: 断言失败,实际结果与预期结果不符".format(case_name))
        '''判断预期与实际接口Data内的参数是否一致，不一致报错,并将报错信息记录到日志内'''
        va = validators.Draft4Validator(expect_schema)
        va.validate(response.json())
        logging.info('模块名称: {},参数必填项校验结果: 成功！'.format(case_name))
        return response.json()
    except jsonschema.exceptions.ValidationError:
        logging.error("模块名称: {},响应体断言结果: 断言失败,实际结果与预期结果不符".format(case_name))
        assert 1 > 2, "模块名称: {},响应体断言结果: 断言失败,实际结果与预期结果不符".format(case_name)
