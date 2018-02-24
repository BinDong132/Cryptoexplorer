import urllib.request
from bs4 import BeautifulSoup


name = input("What's the name?")
link = 'https://info.binance.com/en/currencies/'+name
request = urllib.request.Request(link)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response,'html.parser')
text = soup.get_text()
start = text.find('Introduction')   # start location for introduction
end = text.find('\n\n\n',start)
Introduction = text[start:end]