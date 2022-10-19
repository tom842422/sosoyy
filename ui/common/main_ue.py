# -*- coding: utf-8 -*-
# @Time : 2022/8/13 1:19
# @Author : TOM
# @Email : wayne_lau@aliyun.com
# @File : main_ue.py
# @Project : sosoyy_ui_new

from time import sleep
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from ui.page_location.login_location import LoginLocathin as LL
from ui.page_location.home_location import HomeLocathin as HL
from selenium.webdriver.support import expected_conditions as EC
from ui.page_location.price_comparison import PriceComparison as PC
from ui.common.login_ue import LoginUe
import pytest_rerunfailures


class MainUe:

    def __init__(self, driver: WebDriver, hide=10, timeout=15):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait( time_to_wait=hide )
        self.wait = WebDriverWait( self.driver, timeout )

    # 主流程操作
    def main_ue(self):
        self.wait.until( EC.visibility_of_element_located( HL.purchase_teamwork ) )
        # 展开采购协同
        self.driver.find_element( *HL.purchase_teamwork ).click()
        # 采购计划
        self.driver.find_element( *HL.purchase_plan ).click()
        self.wait.until( EC.visibility_of_element_located( HL.import_purchase_plan ) )
        # 导入采购计划
        self.driver.find_element( *HL.import_purchase_plan ).click()
        # 选择供应商分组
        self.wait.until( EC.visibility_of_element_located( HL.chose_group ) )
        self.driver.find_element( *HL.chose_group ).click()
        # 上传
        self.driver.find_element( *HL.upload_file ).click()
        # 上传excel表格
        sleep( 2 )
        send_keys( r"D:\\work_download\\正式\\32.xlsx" )
        sleep( 3 )
        send_keys( '{ENTER}' )
        # 渠道供应商未加入询价确认框
        self.wait.until( EC.visibility_of_element_located( HL.channel_supplier_inquiry ) )
        self.driver.find_element( *HL.channel_supplier_inquiry ).click()
        # 渠道供应商是否需要报价确认框
        self.driver.find_element( *HL.channel_supplier_offer ).click()
        # 偏好设置确认框
        self.wait.until( EC.visibility_of_element_located( HL.preference_set ) )
        self.driver.find_element( *HL.preference_set ).click()
        return self

    def get_reset(self):
        # 提交采购计划成功校验-提取重置文本
        self.driver.switch_to.frame( "iframe" )
        self.wait.until( EC.visibility_of_element_located( PC.reset ) )
        return self.driver.find_element( *PC.reset_text ).text


if __name__ == '__main__':
    re = MainUe()
