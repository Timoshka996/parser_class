from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        get = urllib.request.urlopen(self.url)
        self.raw_html = get.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('div', class_="td-category-grid")

        for item in news:
            title = item.find('div', class_="product_text pull-left").get_text(strip=True)
            desc = item.find('div', class_="td-post-content").get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость №{i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}')
                i +=1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
