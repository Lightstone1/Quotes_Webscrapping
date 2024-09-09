from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as soup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = UReq(quotes_page)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class": "quotes"})

for quote in quotes:
    fav_quote = quote.findAll("p", {"class": "aquote"})
    aquote = fav_quote[0].text.strip()
    
    fav_authors = quote.findAll("p", {"class": "author"})
    author = fav_authors[0].text.strip()
    
    print(aquote)
    print(author)



SAVING FILES

/*PS C:\Users\USER\Desktop\data science projects\Webscrapping> python quotes.py >myquotes.txt
PS C:\Users\USER\Desktop\data science projects\Webscrapping> python quotes.py >myquotes.csv*/