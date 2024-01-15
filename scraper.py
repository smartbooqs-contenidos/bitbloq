import requests

html = requests.get("https://bitbloq.cc").text

html = html.replace("/_next/", "https://bitbloq.cc/_next/")
html = html.replace("/icons/", "https://bitbloq.cc/icons/")

file = open("docs/index.html", "w")
file.write(html)
file.close()
