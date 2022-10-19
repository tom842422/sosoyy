# -*- coding: utf-8 -*-
# @Time : 2022/8/12 23:22
# @Author : TOM
# @Email : wayne_lau@aliyun.com
# @File : home_location.py
# @Project : sosoyy_ui_new

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeLocathin:
    # ==============首页界面================
    # 获取目前登录账号
    login_num = (By.XPATH, '//*[@id="topNav"]/div[2]/div/a/span[1]')
    # 菜单-采购协同
    purchase_teamwork = (By.XPATH, '//*[@id="leftMenu"]/ul/li[2]/div')
    # 菜单-采购计划
    purchase_plan = (By.XPATH, '//*[@id="sub_menu_1_$$_1-popup"]/li[1]/span/a')
    # ==============采购计划上传流================
    # 原脚本中跳转采购计划方式
    """
    WebDriverWait(browser, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, 'pageContent')))
    """
    # 导入采购计划
    import_purchase_plan = (By.XPATH, '/html/body/div[1]/div/div/div[2]/'
                                      'div[2]/div[1]/div[4]/div[1]/div/button[1]')
    # 上传采购计划中选择供应商分组
    chose_group = (
        By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/button')
    # 上传计划按钮
    upload_file = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[1]')
    # 渠道供应商未加入询价确认框
    channel_supplier_inquiry = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]')

    # 渠道供应商是否需要报价确认框
    # channel_supplier_offer = (By.CSS_SELECTOR, '/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]')
    channel_supplier_offer = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/button[2]')
    # 偏好设置确认框
    preference_set = (By.XPATH, '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]')
    # preference_set = (By.XPATH, '/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button[2]')
    # 自定义字段全选按钮
    chose_all_custom = (
        By.XPATH, '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/label/span[1]/input')
    # 自定义字段确认
    ident_custom = (By.XPATH, '/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]')
