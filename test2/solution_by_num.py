from search_dream import *

def solution_by_num(num, hrefs): #리턴값은 꿈해몽 전문

    url = hrefs[num]

    driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver_win32\chromedriver.exe')
    # 웹사이트 열기
    driver.get(url)

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    solution = ""
    count = 1
    for i in soup.find_all('div', class_="grayBg"):
        if count == 1:
            solution = i.get_text().strip()
            count +=1
    # print(solution)
    return solution

# print(searchDream('바다'))
# solution_by_num(26, searchDream('바다'))