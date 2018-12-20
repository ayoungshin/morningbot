from selenium import webdriver
from bs4 import BeautifulSoup

def searchDream(text):
    driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver_win32\chromedriver.exe')
    # 웹사이트 열기
    driver.get('https://fortune13.nate.com/v1/dream/dream/dream.asp?1=1')
    # 검색창 찾기
    search_text = driver.find_element_by_css_selector('input#memo.inT')
    # 검색바에 우유 적기
    search_text.send_keys(text)

    btn = driver.find_element_by_id('btnSearch')
    btn.click()

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    titles = []
    title_nums = []
    href_list = []
    pre_url = 'https://fortune13.nate.com/v1/dream/dream/'
    for i in soup.find_all('td', class_="tit"):
        href_list.append(pre_url + i.find('a')['href'])
        titles.append(i.get_text().strip())
    for n in soup.find_all('td', class_="num"):
        title_nums.append(int(n.get_text().strip()))
    result_list = []
    print('{}{}'.format(href_list[0],titles[0]))
    for i in range(len(titles)):
        result_list.append('<{}|{}>'.format(href_list[i], titles[i]))
    # num_to_title = dict(zip(title_nums, titles))
    # num_to_href = dict(zip(href_list, titles))
    # href_to_title = dict(zip(href_list, titles))

    return result_list
print(searchDream('바다'))

# 꿈 - 입력대기 - 서치드림(입력값) -

