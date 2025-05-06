# File: crawler.py
import wikipedia
from bs4 import BeautifulSoup
import requests
import os
from config import RAW_TEXT_DIR

def crawl_wikipedia(person_name, sentences=50):
    try:
        page = wikipedia.page(person_name)
        text = page.content
    except wikipedia.DisambiguationError:
        text = wikipedia.summary(person_name)
    paras = [p for p in text.split("\n\n") if len(p) > 100]
    return paras[:sentences]

def crawl_news(person_name, num_articles=5):
    # 예시: 네이버 뉴스 검색 크롤러
    headers = {"User-Agent": "Mozilla/5.0"}
    query = requests.utils.quote(person_name + " 기사")
    url = f"https://search.naver.com/search.naver?&where=news&query={query}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = [a["href"] for a in soup.select("a.news_tit")][:num_articles]
    contents = []
    for link in links:
        r = requests.get(link, headers=headers)
        s = BeautifulSoup(r.text, "html.parser")
        article = "\n".join([p.get_text() for p in s.select("div#articleBodyContents p")])
        if len(article) > 100:
            contents.append(article)
    return contents

if __name__ == "__main__":
    persons = ["손흥민", "이재명"]
    os.makedirs(RAW_TEXT_DIR, exist_ok=True)
    for person in persons:
        paras = crawl_wikipedia(person)
        with open(os.path.join(RAW_TEXT_DIR, f"{person}.txt"), "w", encoding="utf-8") as f:
            f.write("\n\n".join(paras))
        news = crawl_news(person)
        with open(os.path.join(RAW_TEXT_DIR, f"{person}_news.txt"), "w", encoding="utf-8") as f:
            f.write("\n\n".join(news))
