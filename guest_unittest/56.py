"""
封装定位器
"""
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginpageLocator():
    """
    用户登录界面
    """
    Username = (By.ID, "usernmae")  # 登录名
    Password = (By.ID, "password")  # 密码
    LoginButton = (By.ID, "login-submit")  # 登录按钮
    loginname = (By.ID, "loggedas")  # 登陆后用户名
    loginFaidmsg = (By.ID, "flash_error")  # 登录失败信息


class Projectlist():
    """
    项目列表页
    """
    NewProject = (By.LINK_TEXT, "新建项目")  # 新建项目按钮


class NewprojectPage():
    """
    新建项目页面
    """
    ProjectName = (By.ID, "project_name")  # 项目名称
    CommitButton = (By.NAME, 'commit')  # 提交按钮
    Commitinfo = (By.ID, "flash_notice")  # 提交信息


"""
一个页面元素对应一个类
该类下编写元素定位器
"""
"""
封装元素操作层，首先导入页面定位器，当前在同一文件内，所以不必再次导入
"""


class BasePage():
    def __init__(self, driver):
        # 初始化时会自动执行
        self.driver = driver


class LoginPage(BasePage):
    """
    用户登录页面的操作
    """

    def enter_username(self, username):
        """
        输入用户名
        """
        ele = self.driver.find_element(*LoginpageLocator.Username)
        ele.clear()
        ele.send_keys(username)

    def enter_password(self, password):
        """
        输入密码
        """
        ele = self.driver.find_element(*LoginpageLocator.Password)
        ele.clear()
        ele.send_keys(password)

    def click_login_button(self, login_button):
        """
        单击登录按钮
        """
        ele = self.driver.find_element(*LoginpageLocator.LoginButton)
        ele.clear()
        ele.send_keys(login_button)


"""
封装登陆页面测试用例,首先导入页面操作，当前在同一文件内，所以不必导入
"""


class test_login():
    """
    登录页面场景
    """
    def login_page_test(self):
        url = "http://localhost:8080/login"
        username = "zhangsan"
        password = "123456"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        LoginPage(driver).enter_username(username)
        LoginPage(driver).enter_password(password)
        LoginPage(driver).click_login_button()
        return driver
if __name__ == '__main__':
    test_login().login_page_test()
