import os
import time

import pytest

if __name__ == '__main__':
    # pytest.main(['-s', '-v'])
    pytest.main(['-v', '-s', 'testcases/test_mimu.py::TestMain::test_mimu_api'])
    time.sleep(2)
    # # 生成allure测试报告
    os.system("allure generate ./temps -o ./reports --clean")
