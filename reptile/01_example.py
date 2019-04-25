from urllib.request import urlopen

# if has Chinese, apply decode()  以下就是所要爬的网址链接，可根据需要修改
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])


res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)