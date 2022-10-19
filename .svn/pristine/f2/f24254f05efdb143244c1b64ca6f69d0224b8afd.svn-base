from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from ui.page_location.login_location import LoginLocathin as LL
from ui.page_location.home_location import HomeLocathin as HL
from selenium.webdriver.support import expected_conditions as EC

class LoginUe:

    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout)

    # 登录页面定位及操作
    def login_ue(self, user, pw):
        self.wait.until(EC.visibility_of_element_located(LL.login_button))
        self.driver.find_element(*LL.login_user_input).send_keys(user)
        self.driver.find_element(*LL.login_passwd_input).send_keys(pw)
        self.driver.find_element(*LL.login_code_input).send_keys('2usw')
        self.driver.find_element(*LL.login_button).click()
        return self

    def get_login_num(self):
        return self.driver.find_element(*HL.login_num).text

    def get_login_success_01(self):
        # 登录校验
        self.wait.until(EC.visibility_of_element_located(HL.login_num))
        return self.driver.find_element(*HL.login_num).text

    def get_login_false_01(self):
        # 登录失败
        self.wait.until(EC.visibility_of_element_located(LL.login_false))
        return self.driver.find_element(*LL.login_false).text


if __name__ == '__main__':
    re = LoginUe()
