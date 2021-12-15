#%%
from browsermobproxy import Server
from browsermobproxy import Client
import psutil
import time


# for proc in psutil.process_iter():
#     # check whether the process name matches
#     if proc.name() == "browsermob-proxy":
#         proc.kill()

# dict = {"port": 8090}
# server = Server(path="../../browsermob-proxy-2.1.4/bin/browsermob-proxy", options=dict)
# server.start()
# time.sleep(1)
# proxy = server.create_proxy()

proxy = Client("localhost:8090")
#%%
# time.sleep(1)
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# options = webdriver.ChromeOptions()
options = Options()
# options = Options()
# options.add_argument("--proxy-server={}".format(client.proxy))
# options.add_argument("--ignore-certificate-errors")
# options.headless = True
# driver = webdriver.Firefox(options=options)
# print("--proxy-server={}".format(proxy.proxy))
# options.add_argument("--proxy-server={}".format(proxy.proxy))
# print(options.proxy)
# options.proxy = proxy.selenium_proxy()
PROXY = proxy.proxy  # "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX["proxy"] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}
# options.add_argument("--ignore-certificate-errors")
options.headless = True
driver = webdriver.Firefox(options=options)
# chromePath = "/home/su/app/crawler/stock_post_crawler/chromedriver"
# driver = webdriver.Chrome(executable_path=chromePath, chrome_options=options)
# profile = webdriver.FirefoxProfile()
# selenium_proxy = proxy.selenium_proxy()
# profile.set_proxy(selenium_proxy)
# driver = webdriver.Firefox(firefox_profile=profile)
#%%
import pprint

proxy.new_har(options={"captureContent": True})
driver.get("https://music.163.com/#/search/m/?s=%E5%91%A8%E6%9D%B0%E4%BC%A6")
# time.sleep(3)
res = proxy.har
# print(proxy.har)  # returns a HAR JSON blob
driver.close()
#%%
# driver.get_screenshot_as_file("test3.png")
# server.stop()
driver.quit()
# %%
import json

json_d = json.loads(
    [
        one
        for one in res["log"]["entries"]
        if one["request"]["url"]
        == "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    ][0]["response"]["content"]["text"]
)
pprint.pprint(json_d)
# %%
