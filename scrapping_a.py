import bs4 as bs
import urllib.request

url = input('Enter the URL - ')
print('\nURL   : ',url)
html = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(html, 'lxml')
print('Title : ',soup.title.string)	
print()
#----------EXAMPLE ------------	
tags = soup('a')
count = 0
for tag in tags:
	count += 1
	print(count, ' - ' ,tag.get('href'))
	
#----------EXAMPLE ------------
#print(soup.get_text())
# print(soup.a)
# print(soup.p)
# print(soup.find_all('pre'))

#----------EXAMPLE ------------
# tags = soup('pre')
# for tag in tags:
	# print(tag.text)

	
