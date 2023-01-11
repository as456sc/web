from fake_useragent import UserAgent
import bs4
import requests



KEYWORDS = ['дизайн', 'фото', 'web', 'Python']



URL = "https://habr.com/ru/all/"

ua = UserAgent()
HEADERS = {'User-Agent': ua.safari}


response = requests.get(URL, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text,  features="html.parser")
articls  = soup.find_all("article")



for article in articls:
    datetime_published = article.find("time").get("title")
    pars_keywords = article.find_all(class_="tm-article-snippet")
    pars_keywords = " ".join([pars_keyword.text.strip() for pars_keyword in pars_keywords])
    link = article.find(class_="tm-article-snippet__title-link").get("href")
    for search_word in KEYWORDS:
        if search_word in pars_keywords:
           print(f"Дата - {datetime_published}; Заголовок - {search_word}; Ссылка - {URL}{link}")






























        







