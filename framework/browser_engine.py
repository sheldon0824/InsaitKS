import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BrowserEngine").get_log()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    # on Windows OS is using xxx.exe, while on macOS will using unix chrome driver(without extension)
    chrome_driver_path_win = dir + '/tools/chromedriver.exe'
    chrome_driver_path_mac = dir + '/tools/chromedriver'
    firefox_driver_path = dir + '/tools/geckodriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    # C:\Users\艺东Sheldon\PycharmProjects\automation_framework_demo\tools
    # print(chrome_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # 从配置文件读取 system_os 和 browser type
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        config_file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # config.read(config_file_path)
        config.read(config_file_path, encoding='UTF-8')   # 解决配置文件中有中文解码出错的问题

        system_os = config.get("systemOS", "OSName")
        logger.info("Your are running on %s operating system" % system_os)
        browser = config.get("browserType", "browserName")
        logger.info("You have selected %s browser " % browser)
        url = config.get("testServer", "URL")
        logger.info("You have input URL %s " % url)
        
        if system_os == 'Mac':
            driver = webdriver.Chrome(self.chrome_driver_path_mac)
            logger.info('Launching Chrome on MacOS now.')
        else:
            if browser == 'Firefox':
                driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
                logger.info('Launching Firefox now.')
            elif browser == 'IE':
                driver = webdriver.Ie(self.ie_driver_path)
                logger.info('Launching IE now.')
            elif browser == 'Chrome':
                driver = webdriver.Chrome(self.chrome_driver_path_win)
                logger.info('Launching Chrome on Windows now.')

        driver.get(url)
        logger.info("Opening %s" % url)
        driver.maximize_window()
        driver.implicitly_wait(3)
        logger.info("Set implicitly wait 3 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Going to close and quit the browser.")
        self.driver.quit()







