import allure
import pytest

from common.login_ue import LoginUe
# from common.login_ue import driver as DR
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    driver.get('https://srm.sosoyy.com')
    # driver.get(url='http://192.168.1.50/')
    yield driver
    driver.close()


@allure.feature('登录模块')
class TestLogin:
    @allure.step('登录成功')
    def test_login_ue_success_01(self, get_driver):
        LoginUe(get_driver).login_ue('13518101893', '123456')  # 正式数据
        assert LoginUe(get_driver).get_login_num() == '13518101893'

    @allure.step('密码错误,登录失败')
    def test_login_ue_false_02(self, get_driver):
        LoginUe(get_driver).login_ue('13518101893', '123457')
        assert LoginUe(get_driver).get_login_false() == '登录失败，账号或密码错误'


if __name__ == '__main__':
    re = TestLogin()
