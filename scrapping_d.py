import bs4 as bs
import urllib.request
import pandas as pd

url = input('Enter the URL - ')
print('\nURL  : ',url)
print()

#----------EXAMPLE ------------
# dfs = pd.read_html(url, header=0)
# for df in dfs:
	# print(df)
	
#----------EXAMPLE Sitemap.xml------------	
xml = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(xml, 'xml')
count = 0
for x in soup.find_all('loc'):
	count += 1
	print(count, '-' ,x.text)