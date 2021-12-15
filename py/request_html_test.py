#%%
from requests_html import HTMLSession

session = HTMLSession()
r = session.get(
    "https://music.163.com/#/search/m/?s=%E5%91%A8%E6%9D%B0%E4%BC%A6&type=1000"
)

r.html.render()
# frame = r.html.find("iframe", first=True)
# print(frame.html)
with open("content2.html", "w") as f:
    f.write(r.content.decode())

# %%
