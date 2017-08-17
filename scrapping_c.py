import bs4 as bs
import urllib.request

url = input('Enter thr URL - ')
print('\nURL  : ',url)
html = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(html, 'lxml')
print()
#----------EXAMPLE ------------
# table = soup.table
# print(table)

#----------EXAMPLE ------------
table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows:
	td = tr.find_all('td')
	row = [x.text for x in td]
	print(row)