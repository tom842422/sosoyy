# -*- coding: utf-8 -*-
# @Time : 2022/8/12 23:00
# @Author : TOM
# @Email : wayne_lau@aliyun.com
# @File : test_main_ue.py
# @Project : sosoyy_ui_new
from time import sleep

import allure
import pytest
from selenium import webdriver

from ui.common.login_ue import LoginUe
from ui.common.main_ue import MainUe


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    driver.get( 'https://srm.sosoyy.com' )
    # driver.get(url='http://192.168.1.50/')
    yield driver
    driver.close()


@allure.feature( '主流程-非多门店-普通采购计划提交（不含报价）' )
class TestMainUe:
    @allure.step( '成功' )
    def test_main_ue_03(self, get_driver):
        LoginUe( get_driver ).login_ue( '13518101893', '123456' )  # 正式数据
        MainUe( get_driver ).main_ue()
        assert MainUe( get_driver ).get_reset() == '重置'


if __name__ == '__main__':
    res = TestMainUe()
