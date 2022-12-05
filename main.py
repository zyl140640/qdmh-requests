import os
import time

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v'])
    time.sleep(2)
    # # 生成allure测试报告
    os.system("pytest testcases/test_mimu.py -s -q  --alluredir=./result/")
    os.system("allure generate ./result/ -o ./reports  --clean")
