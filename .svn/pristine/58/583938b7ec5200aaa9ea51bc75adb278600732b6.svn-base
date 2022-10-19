import pytest
import sys,os

# 在cmd切换到项目目录下输入 allure generate report/ -o report/html --clean 生成html报告

sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# path.insert(0, p.dirname(p.dirname(p.abspath(__file__))))
if __name__ == '__main__':
    pytest.main(['-v', '-k ', '--alluredir=./report', '--clean-alluredir'])
    # os.system('allure generate report/ -o report/html --clean')
