from bs4 import BeautifulSoup
import os
import pandas as pd
import glob


if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing:",one_file_name)
	scraping_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(",html","")
	f = open(one_file_name,"r",encoding = "utf-8")
	#f = open("html_files/coinmarketcap20200202151527.html","r",encoding = "utf-8")
	soup = BeautifulSoup(f.read(),"html.parser")


	#html_content = f.read()
	#soup = (html_content,"html.parser")
	f.close()
	#print(soup)

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find("tr")

	for r in currency_rows:
		currency_price = r.find('td',{"class":"cmc-table__cell--sort-by__price"}).find("a").text.replace(",","").replace("$","")
		currency_name = r.find('td',{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
		currency_marketcap = r.find('td',{"class":"cmc-table__cell--sort-by__market-cap"}).find("div").text.replace("$","")
		currency_supply = r.find('td',{"class":"cmc-table__cell--sort-by__circulating-supply"}).find("div").text.replace("*","").replace("$","")
		# print(currency_name)
		# print(currency_price)
		# print(currency_marketcap)
		# print(currency_supply)
		df = df.append({
			'time': scraping_time,
			'name': currency_name,
			'price': currency_price,
			'marketcap': currency_marketcap,
			'supply': currency_supply
		}, ignore_index=True)



# print(df)
# df.to_csv("parsed_files/coinmarketcap_dataset.csv")
