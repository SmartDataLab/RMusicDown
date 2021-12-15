from browsermobproxy import Server
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
import pprint


class ProxyManger:

    __BMP = "../../browsermob-proxy-2.1.4/bin/browsermob-proxy"

    def __init__(self):

        self.__server = Server(ProxyManger.__BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):

        self.__client = self.__server.create_proxy()
        # params={"trustAllServers": "true"}
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server


if __name__ == "__main__":
    # 开启Proxy
    proxy = ProxyManger()
    server = proxy.start_server()
    time.sleep(1)

    client = proxy.start_client()

    # 配置Proxy启动WebDriver
    options = webdriver.ChromeOptions()
    # options = Options()
    options.add_argument("--proxy-server={}".format(client.proxy))
    options.add_argument("--ignore-certificate-errors")
    # options.headless = True
    # driver = webdriver.Firefox(options=options)
    chromePath = "/home/su/app/crawler/stock_post_crawler/chromedriver"
    driver = webdriver.Chrome(executable_path=chromePath, chrome_options=options)

    # 获取返回的内容
    client.new_har("baidu.com")
    driver.get("https://www.baidu.com/")
    time.sleep(3)

    newHar = client.har
    pprint.pprint(newHar)
    server.stop()