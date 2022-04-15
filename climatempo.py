from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


req = Request('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

#html = urlopen("https://www.climatempo.com.br/")

soup = BeautifulSoup(html, 'html.parser')


#print(soup.prettify())

#<span class="-text -bold -gray-dark-2 -font-55 _margin-l-15" id="current-weather-temperature">22°</span>
#<span class="temperature _margin-l-5 -font-13">22°</span>
#temperatura = soup.find("span", class_="temperature _margin-l-5 -font-13")
#<span class="city _margin-r-5 -font-13">São Paulo, SP</span>
#<span class="-gray-light" id="min-temp-1">20°</span>
#<span class="-gray-light" id="max-temp-1">30°</span>
#<span itemprop="name">São Paulo - SP</span>

minima = soup.find('span', attrs={'id': 'min-temp-1'}).text.strip()
print(minima)

maxima = soup.find('span', attrs={'id': 'max-temp-1'}).text.strip()
print(maxima)
