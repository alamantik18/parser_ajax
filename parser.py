from requests import Session
from bs4 import BeautifulSoup
import time, random

base_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'
}

def main(base_url):
    session = Session()
    session.headers.update(headers)

    count, pagination = 1, 0
    while True:
        url = base_url + '?page=' + str(count) if count > 1 else base_url

        response = session.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

        if count == 1:
            pagination = int(soup.find('ul', class_="pagination invisible").find_all('li', class_="page-item")[-2].text)

        for card in cards:
            name = card.find('h4', class_="card-title").text
            price = card.find('h5').text
            print(name, price)

        print(count)
        time.sleep(random.choice([3, 5, 7, 9]))
        if count == pagination:
            break

        count += 1

if __name__ == '__main__':
    main(base_url)