import os
import time

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v', "--alluredir", "./result/"])
    time.sleep(2)
    # # 生成allure测试报告
    os.system("allure generate ./result/ -o ./reports  --clean")
#     allure open reports  打开测试报告，启动服务让别人可以访问
