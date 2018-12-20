def findURL(result):
    url = 'urlnono'
    if "쥐" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A5%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "소" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%86%8C%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "호랑이" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%98%B8%EB%9E%91%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "토끼" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%86%A0%EB%81%BC%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "용" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9A%A9%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "뱀" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B1%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "말" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%A7%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "양" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%96%91%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "원숭이" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9B%90%EC%88%AD%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "닭" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8B%AD%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "개" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B0%9C%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "돼지" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8F%BC%EC%A7%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
    elif "물병" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%AC%BC%EB%B3%91%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "물고기" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "양" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%96%91%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "황소" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%99%A9%EC%86%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "쌍둥이" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%8C%8D%EB%91%A5%EC%9D%B4%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "사자" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%82%AC%EC%9E%90%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "게" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B2%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "처녀" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%B2%98%EB%85%80%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "천칭" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%B2%9C%EC%B9%AD%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "전갈" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B0%88%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "염소" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%97%BC%EC%86%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    elif "사수" in result:
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%82%AC%EC%88%98%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"

    return url
