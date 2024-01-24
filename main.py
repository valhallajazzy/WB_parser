import requests
from urllib.parse import urlencode
from math import ceil
import random

CONST_HEADERS = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
}


def get_count_positions(keyword, const_headers=CONST_HEADERS):

    url = f'https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-1257786&filters=xsubject&{urlencode({"query": keyword})}&resultset=filters&spp=29&suppressSpellcheck=false'

    headers = {
        **const_headers,
        'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?page=4&sort=popular&{urlencode({"search": keyword})}',
    }
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.json()['data']['total']


def get_all_articles_by_keyword(keyword, count_of_positions, const_headers=CONST_HEADERS):
    all_article_numbers = []
    pages_count = ceil(count_of_positions/100)
    for page in range(1, pages_count+1):
        url = f'https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-1257786&page={page}&{urlencode({"query": keyword})}&resultset=catalog&sort=popular&spp=29&suppressSpellcheck=false'
        headers = {
            **const_headers,
            'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?page={page}&sort=popular&{urlencode({"search": keyword})}',
        }
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        positions_by_page = response.json()['data']['products']
        articles_by_page = [position['id'] for position in positions_by_page]
        all_article_numbers.extend(articles_by_page)

    return all_article_numbers


def find_position_in_search(all_articles, target_article):
    target_article = int(target_article)
    if target_article in all_articles:
        return all_articles.index(target_article)+1
    else:
        return 'Данного артикула нет в искомой ключевой фразе'


def main():
    target_article = input('Введите артикул: ')
    keyword = input('Введите ключевую фразу: ')
    count_of_positions = get_count_positions(keyword)
    all_article_numbers = get_all_articles_by_keyword(keyword, count_of_positions)
    position = find_position_in_search(all_article_numbers, target_article)
    print(position)


if __name__=='__main__':
    main()


