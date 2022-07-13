from bs4 import BeautifulSoup as soup

def extract_data(html):
    page_soup = soup(html, "html.parser")

