# -*- coding: utf-8 -*-
# @Time : 2022/8/13 1:55
# @Author : TOM
# @Email : wayne_lau@aliyun.com
# @File : price_comparison.py
# @Project : sosoyy_ui_new
from selenium.webdriver.common.by import By


class PriceComparison:
    # 询比价页面-重置
    reset = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/button[2]')
    # 重置确认
    ident_reset = (By.XPATH, '//*[@id="app"]/div/div[14]/div/p[2]/button[2]')
    # ident_reset = (By.XPATH,
                   # '#app > div > div.content.container.commonEdit > div.box > div.box_header.row > div.shortcut.text-right.col-xs-6.col-md-6.pull-right > button.btn.btn-default.fa.fa-refresh')
    # 重置文本
    reset_text = (By.CSS_SELECTOR,
                  '#app>div>div.content.container.commonEdit>div.box>div.box_header.row > div.shortcut.text-right.col-xs-6.col-md-6.pull-right > button.btn.btn-default.fa.fa-refresh>i')
