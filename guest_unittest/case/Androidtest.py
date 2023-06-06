from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from unittestreport import TestRunner
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'mi', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
  'appActivity': '.MainActivityV2', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(20)
class BaseOpera(object):
    '''
    基础操作
    '''
    def __init__(self, driver):
        self.driver = driver
        self.duration = 1000

    @property
    def width(self):
        '''获取屏幕宽度'''
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        '''获取屏幕高度'''
        return self.driver.get_window_size()['height']

    def swipe_to_left(self, base=0.1):
        '''从右向左滑动'''
        return self.driver.swipe(self.width*(1-base),
                                    self.height*0.5,
                                    self.width*base,
                                    self.height*0.5,
                                    self.duration
                                    )

    def swipe_to_right(self, base=0.1):
        '''从左向右滑动'''
        return self.driver.swipe(self.width*base,
                                    self.height*0.5,
                                    self.width*(1-base),
                                    self.height*0.5,
                                    self.duration
                                    )

    def swipe_to_top(self, base=0.9):
        '''从下向上滑动'''
        return self.driver.swipe(self.width*0.5,
                                    self.height*base,
                                    self.width*0.5,
                                    self.height*(1-base),
                                    self.duration
                                    )

    def swipe_to_bottom(self, base=0.9):
        '''从上向下滑动'''
        return self.driver.swipe(self.width*0.5,
                                    self.height*(1-base),
                                    self.width*0.5,
                                    self.height*base,
                                    self.duration
                                    )
class Test_Android(unittest.TestCase):
  def test_android_001(self):
      """
      BIliBili 搜索课程，并获取课程明细
      """
  # 连接Appium Server，初始化自动化环境


      # # 设置缺省等待时间
      # driver.implicitly_wait(5)
      #
      # # 如果有`青少年保护`界面，点击`我知道了`
      # iknow = driver.find_elements(By.ID, "text3")
      # if iknow:
      #     iknow.click()
      #
      # # 根据id定位搜索位置框，点击

      driver.find_element(By.ID, 'expand_search').click()
      #
      # # 根据id定位搜索输入框，点击
      #time.sleep(3)
      sbox = driver.find_element(By.ID, 'tv.danmaku.bili:id/search_src_text')
      sbox.send_keys('白月黑羽')
      # # 输入回车键，确定搜索
      driver.press_keycode(AndroidKey.ENTER)

      #time.sleep(3)

      driver.find_element(By.ID, 'tv.danmaku.bili:id/up_title').click()


      #time.sleep(3)
      #
      video=[]
      #videoslist=list(set(video))
      # # 选择（定位）所有视频标题
      #for i in range(9):
      #driver.swipe(width * 0.5, height * 0.1, width * 0.5, height * 0.9, 1000)

      for i in range(10):
          bo = BaseOpera(driver)
          bo.swipe_to_top()

          eles = driver.find_elements(By.ID,'tv.danmaku.bili:id/title')


          for ele in eles:
             video.append(ele.text)
      print(list(set(video)))
      print("总计视频{}条".format(len(list(set(video)))))
      #print("总计视频{}条".format(len(video)))
            #print(ele.text)

      #return video
          # #
      # input('**** Press to quit..')
      # driver.quit()
      # # 运行代码前，要先 运行 Appium Desktop
      # #
      # # 上面的代码只是抓取一页视频标题，要自动化滚动抓取所有的视频标题。
      # #
      # # Appium 2 的 find_element写法
      # # 注意：Appium Python 现在已经升级到 2.x 大版本，依赖 Selenium 4 以后， 下面这种 find_element_by* 方法都作为过期不赞成的写法
      #
      # driver.find_element_by_id('username').send_keys('byhy')
      # # 运行会有告警，都要写成下面这种格式
      #
      # from selenium.webdriver.common.by import By
      #
      # wd.find_element(By.ID, 'username').send_keys('byhy')
      #
      # # 而后续还有 Appium独有的查找方式，比如
      #
      # # driver.find_element_by_accessibility_id('byhy')
      # # driver.find_element_by_android_uiautomator(code)
      # # 要改成
      #
      # from appium.webdriver.common.appiumby import AppiumBy
      #
      # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'byhy')
      # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
      #
      # # 这样也可以根据ID
      # wd.find_element(AppiumBy.ID, 'username').send_keys('byhy')
# if __name__ == '__main__':
#   suite = unittest.TestSuite()
#   suite.addTest(Test_Android('test_android_001'))
#
#   with open('./hTestReport.html','wb') as report:
#     runnner=HTMLTestRunner(stream=report,title="bili 视频LIST",description="用例执行情况",verbosity=2)
#     runnner.run(suite)
#
 


  # runnner=TestRunner(suite)
  # runnner.run()