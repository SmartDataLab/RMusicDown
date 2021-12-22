#%%
from os import read
import sqlite3
from datetime import date, datetime
from fastapi import FastAPI
from requests import api
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import quote, unquote

app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_path = "../data/recommend.db"
#%%
from browsermobproxy import Server
from browsermobproxy import Client
import psutil
import time

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

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

# 系统自动更新导致driver不能用了
options = webdriver.ChromeOptions()
# options = Options()
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

from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_sele = Proxy(
    {
        "proxyType": ProxyType.MANUAL,
        "httpProxy": PROXY,
        "noProxy": "",  # set this value as desired
    }
)

#          driver = webdriver.Firefox(executable_path=path,options=options,proxy=proxy )
webdriver.DesiredCapabilities.FIREFOX["proxy"] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}

# options.add_argument("--ignore-certificate-errors")
#%%


# Use the `install()` method to set `executabe_path` in a new `Service` instance:
# service = Service(executable_path=GeckoDriverManager().install())

# options=options, executable_path="./geckodriver 2"

# driver = webdriver.Chrome(options=options)
# chromePath = "/home/su/app/crawler/stock_post_crawler/chromedriver"
# driver = webdriver.Chrome(executable_path=chromePath, chrome_options=options)
# profile = webdriver.FirefoxProfile()
# selenium_proxy = proxy.selenium_proxy()
# profile.set_proxy(selenium_proxy)
# driver = webdriver.Firefox(firefox_profile=profile)
#%%
import pprint
import json


def get_new_query_data(query):
    # options.add_argument("--ignore-certificate-errors")
    service = Service(
        executable_path="/home/su/.wdm/drivers/geckodriver/linux64/v0.30.0/geckodriver"
        # executable_path="../geckodriver 2"
    )
    # chrome_options = Options()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service, options=options)
    proxy.new_har(options={"captureContent": True})
    quoted_query = quote(query)
    url = f"https://music.163.com/#/search/m/?s={quoted_query}&type=1000"
    print(url)
    driver.get(url)
    time.sleep(2)
    res = proxy.har
    api_request_info = [
        one
        for one in res["log"]["entries"]
        if one["request"]["url"]
        == "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    ][0]
    # get the params and encSecKey
    # Reverse Engineer with AI
    post_data = {
        one["name"]: one["value"]
        for one in api_request_info["request"]["postData"]["params"]
    }
    driver.quit()
    # open connection
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    json_path = f"../query_json/{query}.json"
    c.execute(
        "INSERT INTO QUERY (KEYWORD, PARAMS, ENCSECKEY, JSON_PATH) VALUES(?,?,?,?);",
        (query, post_data["params"], post_data["encSecKey"], json_path),
    )
    conn.commit()
    conn.close()
    json_d = json.loads(api_request_info["response"]["content"]["text"])
    json.dump(json_d, open(json_path, "w"), ensure_ascii=False)
    # close connection
    return json_d


# pprint.pprint(proxy.har)  # returns a HAR JSON blob
#%%


@app.get("/search")
async def query(query: str = "姜云升", mac_address: str = "", choice: int = 1):
    readable_query = unquote(query)
    print(readable_query)
    # open connection
    now = datetime.now()  # current date and time
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(db_path)
    # save the query record into database
    c = conn.cursor()
    c.execute(
        "INSERT INTO REQUEST (KEYWORD, TIME, USER_MAC, CHOICE) VALUES(?,?,?,?);",
        (readable_query, date_time, mac_address, choice),
    )
    # try to search from the database
    c = conn.cursor()
    cursor = c.execute(f"SELECT JSON_PATH FROM QUERY WHERE KEYWORD='{readable_query}';")
    # if it exists load json and return restorn
    # close connection
    json_path = None
    for row in cursor:
        json_path = row[0]
    conn.commit()
    conn.close()
    if json_path != None:
        json_d = json.load(open(json_path))
    # if not new query and return
    else:
        json_d = get_new_query_data(readable_query)
    return json_d


if __name__ == "__main__":
    uvicorn.run(app, port=8084, host="0.0.0.0")
    # driver.close()