import urllib.request
import time
import datetime
import os

if not os.path.exists("html_files"):
	os.mkdir("html_files")

# for i in range(5):
# 	print("hahaha")
# 	time.sleep(5)

# f = open("coinmarketcap.html", "wb")
# response = urllib.request.urlopen("https://coinmarketcap.com/")

# #print(response)

# html = response.read()
# f.write(html)
# f.close()

# #print(html)

for i in range(5):
	#f = open("coinmarketcap" + str(i) + ".html", "wb")
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen("https://coinmarketcap.com/")
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(5)#seconds for example:300
	#time.sleep(3600 + random)# mimic a human





