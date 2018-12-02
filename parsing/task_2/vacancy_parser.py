import requests
from bs4 import BeautifulSoup

from task_2.vacancy_info import VacancyInfo

keywords = ('требования', 'компетенции', 'подходишь', 'если')  # 'если ты', 'если у вас'


def save_file(url):
    filename = url.split('/')[-1] + '.html'
    print(filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers=headers)
    with open(filename, 'wb') as output_file:
        output_file.write(r.text.encode('UTF-8'))
    return filename


def find_title(soup):
    header = soup.find('div', {'class': 'vacancy-title'})
    title = header.find('h1', {'class': 'header'}).text
    salary = header.find('p', {'class': 'vacancy-salary'}).text
    return title, salary


def validate_strong(strong_tag):
    for words in keywords:
        if words in strong_tag.text:
            return True
    pass

def get_li_tags_text(ul_tag):
    lis = []
    for li in ul_tag.find_all('li'):
        lis.append(li.text)
    return lis


def find_requirements(soup):
    reqs = []
    vacancy_description = soup.find('div', {'class': 'vacancy-description'})
    experience = vacancy_description.find('span', {'data-qa': 'vacancy-experience'})
    if experience:
        reqs.append('Опыт работы : %s' % experience.text)
    for strong_tag in vacancy_description.find_all('strong'):
        if validate_strong(strong_tag):
            print(strong_tag)
            parent = strong_tag.parent
            print(parent.parent)
            ul_tag = parent.find_next_sibling('ul')
            if ul_tag:
                for req in get_li_tags_text(ul_tag):
                    reqs.append(req)
                print(ul_tag)

            else:
                ul_tag = parent.parent.find_next_sibling('ul')
                if ul_tag:
                    for req in get_li_tags_text(ul_tag):
                        reqs.append(req)
                    print(ul_tag)


            #print(strong_tag.text)
            #print(parent.find_next_sibling().findChildren())

            pass
        # print('Опыт работы : %s' % experience.text)

    return reqs


def parse_vacancy(url):
    filename = save_file(url)
    with open(filename, 'rb') as input_file:
        text = input_file.read()
    soup = BeautifulSoup(text)
    s = soup

    title, salary = find_title(soup)
    requirements = find_requirements(soup)


    vacancy_info = VacancyInfo(title, salary, requirements)
    print(vacancy_info)
    #print(title, salary)
# todo:


def main():
    url = 'https://career.ru/vacancy/29028072'
    parse_vacancy(url)


if __name__ == '__main__':
    main()
