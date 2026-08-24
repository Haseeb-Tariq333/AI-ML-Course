from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html').text
soup = BeautifulSoup(html_text, 'lxml')
books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    book_name = book.h3.text
    book_price = book.find('p', class_ = 'price_color').text.strip()
    book_availability = book.find('p', class_ = 'instock availability').text.strip()
    print(f"The book {book_name} is {book_availability} for price {book_price}")







