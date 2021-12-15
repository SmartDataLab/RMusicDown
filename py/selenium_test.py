import selenium

# %%
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get(url="https://music.163.com/#/search/m/?s=周杰伦&type=1000")
browser.get_screenshot_as_file("test4.png")
# browser.execute_async_script()
browser.find_element_by_tag_name("body").text
#%%
html = browser.execute_script(
    "return document.getElementsByTagName('html')[0].innerHTML"
)
html
#%%
with open("./selenium_html.html", "w") as f:
    f.write(html)
#%%

size = len(browser.find_elements(By.TAG_NAME, "iframe"))
size
#%%
browser.switch_to.default_content()
#%%
browser.switch_to.frame(0)
#%%
browser.find_elements(By.CLASS_NAME, "ztag")
#%%
browser.page_source
#%%

html = browser.execute_script(
    "return document.getElementsByTagName('html')[0].innerHTML"
)
s = Selector(text=html)
html
#%%
s.css("*::text").getall()
#%%
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "m-search"))
    )
    browser.get_screenshot_as_file("test4.png")
finally:
    print(browser.find_elements_by_css_selector("div::text"))
    browser.quit()
#%%
browser.quit()
#%%
browser.get_screenshot_as_file("test2.png")
s = Selector(text=browser.page_source)
s.css("*::text").getall()
#%%

browser.find_elements_by_css_selector("div::text")
#%%
browser.refresh()
browser.page_source
# %%
time.sleep(1)
browser.find_element_by_css_selector(
    'div#app div.content input[type="text"]'
).send_keys(RUC_ID)
browser.find_element_by_css_selector(
    'div#app div.content input[type="password"]'
).send_keys(RUC_PASSWORD)
browser.find_element_by_css_selector("div#app div.btn").click()
time.sleep(1)
browser.page_source
# %%
browser.find_element_by_css_selector('div.form div[name="area"] input').send_keys(
    "北京市  海淀区"
)

time.sleep(1)
browser.page_source
# %%
browser.find_element_by_css_selector('div.form div[name="area"] input').click()
time.sleep(1)
browser.page_source
# %%
browser.find_element_by_css_selector("div.list-box div.footers a").click()
time.sleep(1)
browser.page_source

# %%
browser.find_element_by_css_selector("div.wapcf-btn.wapcf-btn-ok").click()
time.sleep(1)
#%%
# browser.page_source
print("done")
# %%
browser.get_screenshot_as_file("test.png")