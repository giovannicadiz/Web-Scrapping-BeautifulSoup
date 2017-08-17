import bs4 as bs
import urllib.request

url = input('Enter the URL - ')
print('\nURL   : ',url)
html = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(html, 'lxml')
print()
#----------EXAMPLE ------------
for div in soup.find_all('div', class_='body'):	# specific div class_
	print(div.text)
	
#----------EXAMPLE ------------
# nav = soup.nav
# for x in nav.find_all('a'):
	# print(x.get('href'))

#----------EXAMPLE ------------	
# body = soup.body
# for parrafo in body.find_all('p'):
	# print(parrafo.text)
	
