import os
import requests
from bs4 import BeautifulSoup
import unmarkd

SESSION_TOKEN_ENV_VAR = 'ADVENT_SESSION_TOKEN'
if SESSION_TOKEN_ENV_VAR not in os.environ:
    print(SESSION_TOKEN_ENV_VAR + ' not set.')
    exit(1)

SESSION_TOKEN = os.environ[SESSION_TOKEN_ENV_VAR]

def page_error(page, error):
    print('Encountered an error while parsing the page: ' + error)
    print('Saving the failing page to /tmp/aoc_page_error')
    with open('/tmp/aoc_page_error', 'w+') as f:
        f.write(page)
    exit(1)

PAGE_URL_TEMPLATE = "https://adventofcode.com/{year}/day/{day}"
def get_day_parts(year, day):
    url = PAGE_URL_TEMPLATE.format(year=year, day=day)
    page = str(requests.get(url, cookies={"session":SESSION_TOKEN}).content, encoding='utf8')
    soup = BeautifulSoup(page, 'html.parser')

    main_tags = soup.find_all('main')
    if len(main_tags) == 0:
        page_error(page, 'Missing <main> tag')
    if len(main_tags) > 1:
        page_error(page, 'Found more than one <main> tag')
    main_tag = main_tags[0]

    day_descs = main_tag.find_all('article', {'class':'day-desc'})
    if len(day_descs) == 0:
        page_error(page, 'Found no <article class="day-desc"> in <main>')
    elif len(day_descs) > 2:
        page_error(page, 'Found more than two <article class="day-desc"> in <main>')
    
    # html_to_md_converter = HTML2Text()
    # html_to_md_converter.mark_code = True
    part_1 = unmarkd.unmark(day_descs[0].get_text())
    maybe_part_2 = unmarkd.unmark(day_descs[1].get_text()) if len(day_descs) == 2 else None
    return part_1, maybe_part_2
        



INPUT_URL_TEMPLATE = "https://adventofcode.com/{year}/day/{day}/input"
def get_input(year, day):
    url = INPUT_URL_TEMPLATE.format(year=year, day=day)
    page = str(requests.get(url, cookies={"session":SESSION_TOKEN}).content, encoding='utf8')
    return page
