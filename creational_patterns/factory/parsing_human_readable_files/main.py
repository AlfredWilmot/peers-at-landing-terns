import os

url = "https://www.sciencedaily.com/rss/all.xml"
lynxcmd = f"lynx --dump {url}"
xml = os.popen(lynxcmd).read()
print(xml)
