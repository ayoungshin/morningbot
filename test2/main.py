from selenium import webdriver
from bs4 import BeautifulSoup

# # 크롬 드라이버 설정
# driver = webdriver.Chrome(r"C:\Users\student\Desktop\chromedriver_win32\chromedriver.exe")
#
# # 웹 사이트 열기
# driver.get("http://www.10000recipe.com/recipe/list.html")

# source = driver.page_source
# soup = BeautifulSoup(source, "html.parser")

# 값 가져오기
# for i in soup.find_all("h4", class_="ellipsis_title2"):
#     print(i.get_text())

#검색하기
#만개의 레시피를 들어간다 -> 검색한다 -> 그래서 나온 페이지를 Beautiful soup 으로 찾는다

#검색창 찾기
# searchText = driver.find_element_by_id("srhRecipeText") #id가 있는 경우
# searchText.send_keys("우유")
#
# bt = driver.find_element_by_css_selector("button.btn.btn-default") #클래스만 있는 경우
# bt.click()
#
# source = driver.page_source
# soup = BeautifulSoup(source, "html.parser")
#
# for i in soup.find_all("h4", class_="ellipsis_title2"):
#         print(i.get_text())
#